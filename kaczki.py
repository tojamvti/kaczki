import openpyxl

def ducks():
    heights = []
    widths = []
    
    wb = openpyxl.load_workbook('kaczki.xlsx')
    ws = wb['Arkusz1']
    rows = ws.iter_rows(min_row=1, max_row=21, min_col=1, max_col=2)

    for a, b in rows:
        heights.append(a.value)
        widths.append(b.value)

    MAXIMUM_WIDTH = 50
    
    chickens = list(zip(heights[1:], widths[1:]))
    sorted_chickens = sorted(chickens, key=lambda x: x[0], reverse=True)
    
    total_height = 0
    total_width = 0
    count = 0
    
    for chicken in sorted_chickens:
        if total_width + chicken[1] <= MAXIMUM_WIDTH:
            total_height += chicken[0]
            total_width += chicken[1]
            count += 1
        else:
            break

    print(f"Maximum sum of heights of {count} chickens is {total_height}")

print(ducks())
