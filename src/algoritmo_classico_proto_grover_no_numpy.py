import random
import statistics

# ---------------------------------------------------------------------
# 1. ANALYSIS AND SIMULATION FUNCTIONS (without numpy)
# ---------------------------------------------------------------------

def verifica_tendenza_phi(dataset, tolleranza=2):
    """Checks whether the ratio of the first two elements trends toward Phi."""
    if len(dataset) < 2 or dataset[1] == 0:
        return False
    a, b = dataset[0], dataset[1]
    # Integer deviation: |a*5 - b*8|
    scostamento = abs(a * 5 - b * 8)
    return scostamento <= tolleranza


def _mean(xs):
    return statistics.fmean(xs) if xs else 0.0


def _var(xs):
    # Population variance (same as np.var with default ddof=0)
    return statistics.pvariance(xs) if len(xs) >= 2 else 0.0


def _std(xs):
    return (_var(xs) ** 0.5) if len(xs) >= 2 else 0.0


def simula_output_dl_dinamico(traiettoria):
    """Simulates the output of an adaptive DL model based on state."""
    if not traiettoria or _std(traiettoria) == 0:
        return (random.randint(1, 10), random.randint(1, 10))

    media = _mean(traiettoria)  # bias
    pesi = range(1, len(traiettoria) + 1)  # pesi
    somma_ponderata = sum(x * w for x, w in zip(traiettoria, pesi))
    varianza = _var(traiettoria)

    numeratore = abs(int(somma_ponderata + media)) % 25 + 1
    denominatore = abs(int(varianza * len(traiettoria) + media)) % 25 + 1
    return (numeratore, denominatore)


# ---------------------------------------------------------------------
# 2. CORE ALGORITHM FUNCTIONS (internal logic unchanged)
# ---------------------------------------------------------------------

def matrice_gravita_sottrattiva(input_row):
    lunghezza = len(input_row)
    # matrix [length x length]
    matrice = [[0 for _ in range(lunghezza)] for _ in range(lunghezza)]
    matrice[0] = list(input_row)
    for i in range(1, lunghezza):
        for j in range(lunghezza):
            matrice[i][j] = abs(matrice[i-1][j] - matrice[i-1][j+1]) if j < lunghezza - 1 else matrice[i-1][j]
    return matrice


def matrice_interattiva(c, b):
    if c == 0:
        return [b]
    if b == 0:
        return [c]
    return [c + b, abs(c - b)] if c <= b else [c + b]


def genera_colonne_possibili_con_proto_grover(input_row, elemento_riferimento, parametro_congruenza):
    matrice_frattale = matrice_gravita_sottrattiva(input_row)
    prima_colonna = [r[0] for r in matrice_frattale]
    colonne_c0, colonne_c1 = [], []
    migliore_apice, miglior_scostamento = None, float('inf')
    num_cong, den_cong = parametro_congruenza

    def genera_colonna_ricorsiva(idx_inv, col_parz, c_ini, c_curr):
        nonlocal migliore_apice, miglior_scostamento
        if idx_inv == len(prima_colonna):
            apice = col_parz[-1]
            scostamento = abs(apice * den_cong - elemento_riferimento * num_cong) if elemento_riferimento != 0 else apice
            if scostamento < miglior_scostamento:
                miglior_scostamento, migliore_apice = scostamento, apice
            (colonne_c0 if c_ini == 0 else colonne_c1).append(col_parz.copy())
            return
        b = prima_colonna[len(prima_colonna) - 1 - idx_inv]
        c = c_ini if idx_inv == 0 else c_curr
        for a in matrice_interattiva(c, b):
            col_parz.append(a)
            genera_colonna_ricorsiva(idx_inv + 1, col_parz, c_ini, a)
            col_parz.pop()

    genera_colonna_ricorsiva(0, [], 0, 0)
    genera_colonna_ricorsiva(0, [], 1, 1)
    return migliore_apice, len(colonne_c0), len(colonne_c1)


# ---------------------------------------------------------------------
# 3. PROOF-OF-CONCEPT (PoC) ORCHESTRATOR
# ---------------------------------------------------------------------

def esegui_poc_proto_grover(input_iniziale, depth_max=5, stile_output="debug"):
    """Orchestrates the PoC.

    Parameters:
      - depth_max: number of iterations
      - stile_output:
          * "debug"  -> also prints strategy and counts (historical behavior)
          * "pulito" -> prints only input and final trajectory (no DL/proto-grover in output)
    """
    ha_tendenza_phi = verifica_tendenza_phi(input_iniziale)
    strategia = 'phi_sintonizzato' if ha_tendenza_phi else 'dinamico_adattivo'

    if stile_output == "pulito":
        print("--- PoC ---")
        print(f"Input: {input_iniziale}")
    else:
        print("--- AVVIO PROOF OF CONCEPT (PoC) ---")
        print(f"Dataset iniziale: {input_iniziale}")
        print(("✅" if ha_tendenza_phi else "❌") + f" Strategia: '{strategia}'.")
        print("-" * 40)

    traiettoria_lineare = input_iniziale.copy()
    num_colonne_c0, num_colonne_c1 = 0, 0

    for i in range(depth_max):
        # Note: DL and proto-grover remain in the computation, but with
        # stile_output="pulito" they are not exposed in printed output.
        if strategia == 'phi_sintonizzato':
            parametro_attuale = (8, 5)  # integer approximation of Phi
        else:
            parametro_attuale = simula_output_dl_dinamico(traiettoria_lineare)

        apice_ottimale, num_c0, num_c1 = genera_colonne_possibili_con_proto_grover(
            traiettoria_lineare, traiettoria_lineare[0], parametro_attuale
        )

        if i == depth_max - 1:
            num_colonne_c0, num_colonne_c1 = num_c0, num_c1
        if apice_ottimale is None:
            print("Interruzione: nessun apice valido trovato.")
            break

        traiettoria_lineare = [apice_ottimale] + traiettoria_lineare

    if stile_output == "pulito":
        print(f"Traiettoria: {traiettoria_lineare}")
    else:
        print("\n--- RISULTATO FINALE ---")
        print(f"Strategia utilizzata: {strategia}")
        print(f"Traiettoria lineare finale: {traiettoria_lineare}")
        print(f"Numero di colonne (ultimo ciclo) con |c|=0: {num_colonne_c0}")
        print(f"Numero di colonne (ultimo ciclo) con |c|=1: {num_colonne_c1}")


if __name__ == "__main__":
    input_phi = [3, 2, 1, 1]
    esegui_poc_proto_grover(input_phi, depth_max=25, stile_output="pulito")

    print("\n" + "=" * 50 + "\n")

    input_non_phi = [10, 2, 7]
    esegui_poc_proto_grover(input_non_phi, depth_max=5, stile_output="pulito")
