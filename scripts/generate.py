#!/usr/bin/env python3
import os
import json
import sys
from datetime import datetime

def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "docs"
    output_file = os.path.join(base, "reports.json")

    entries = []

    for name in os.listdir(base):
        path = os.path.join(base, name)

        # Solo carpetas
        if not os.path.isdir(path):
            continue

        # Ignorar carpetas que no sean builds
        if name.startswith("."):
            continue

        # Requiere que tenga index.html dentro
        if not os.path.exists(os.path.join(path, "index.html")):
            continue

        created_at = None
        label = name

        # Intentar parsear el nombre tipo YYYY-MM-DD_HH-mm-build
        try:
            # quitamos el sufijo "-build"
            base_name = name.replace("-build", "")
            dt = datetime.strptime(base_name, "%Y-%m-%d_%H-%M")
            created_at = dt.isoformat()
            # label más bonito
            label = dt.strftime("%Y-%m-%d %H:%M")
        except ValueError:
            pass

        entries.append(
            {
                "id": name,
                "label": label,
                "folder": name,
                "url": f"{name}/index.html",
                "createdAt": created_at,
            }
        )

    # Ordenar descendente por fecha (o por id si no se pudo parsear)
    entries.sort(
        key=lambda x: x["createdAt"] or x["id"],
        reverse=True,
    )

    os.makedirs(base, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"Generated {output_file} with {len(entries)} entries.")

if __name__ == "__main__":
    main()
