from __future__ import annotations
def assign_minutes(day_start, minutes, shifts):
    out = []
    for m in minutes:
        assigned = shifts[-1]["name"] if shifts else None
        for sh in shifts:
            if sh["start"] <= m < sh["end"]:
                assigned = sh["name"]
                break
        out.append({"minute": m, "shift": assigned})
    return out
