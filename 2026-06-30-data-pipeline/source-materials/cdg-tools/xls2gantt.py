from pathlib import Path

import pandas as pd


header = """gantt
    title CDG Process Reengineering
    dateFormat  YYYY-MM-DD
    axisFormat  %d-%m
    todayMarker off
"""

test = """
    section Avvio e perimetro
    Kick-off progetto e allineamento stakeholder (CDG-001) :active, CDG-001, 2026-06-01, 1d
    Definizione perimetro funzionale e tecnico (CDG-002) :task2, after task1, 3d
    Raccolta documentazione esistente (CDG-003) :task3, after task1, 2d
    Impostazione piano di lavoro e governance (CDG-004) :task4, after task2, 2d

    section Assessment AS-IS
    Analisi fonti SAP, Jira, CDG APP (CDG-005) :task5, after task3, 5d
    Mappatura flussi input e dipendenze (CDG-006) :task6, after task5, 5d
    Analisi logiche di calcolo attuali (CDG-007) :task7, after task5, 4d

    section Design TO-BE
    Definizione architettura data pipeline (CDG-008) :task8, after task6, 4d
    Design modello dati e tabelle mapping (CDG-009) :task9, after task8, 5d
    Specifica logiche di trasformazione (CDG-010) :task10, after task7, 6d

    section Sviluppo e Build
    Setup ambiente e repository (CDG-011) :task11, after task8, 2d
    Sviluppo connettori input (CDG-012) :task12, after task11, 8d
    Implementazione logiche Core (CDG-013) :task13, after task10, 10d

    section Test e parallel run
    Unit test e bug fixing (CDG-042) :task42, after task13, 5d
    User Acceptance Test (UAT) (CDG-044) :task44, after task42, 5d
    Go-live readiness review (CDG-046) :milestone, m1, after task44, 0d

    section Go live e hypercare
    Redazione runbook operativo (CDG-047) :task47, after m1, 3d
    Formazione utenti e handover (CDG-048) :task48, after task47, 3d
    Go-live controllato (CDG-049) :milestone, m2, after task48, 0d
    Supporto primo ciclo di chiusura (CDG-050) :task50, after m2, 5d
"""


def main():

    # ['Area', 'Attività', 'Release', 'Effort', 'Owner', 'Completion %',
    #    'Start Date', 'End Date', 'Duration', 'Actual', 'Task', 'Issue Type',
    #    'Depends On', 'Acceptance Criteria']

    with Path("output.gantt").open("w") as out:
        df = pd.read_excel(
            "New_CDG Migration_Project Plan.xlsx",
            sheet_name="03_Project_Plan",
            index_col=0,
        )

        out.write(header)
        section = None
        for row in df.itertuples():
            if row.Area != section:
                section = row.Area
                out.write(f"\n    section {section}\n")
            if row.Index == 1:
                out.write(
                    f"        {row.Attività} :{row.Task}, 2026-06-01, {row.Effort}d\n"
                )
            else:
                deps = row._13.split(",")[-1] if "," in row._13 else row._13
                out.write(
                    f"        {row.Attività} :{row.Task}, after {deps}, {row.Effort}d\n"
                )


if __name__ == "__main__":
    main()
