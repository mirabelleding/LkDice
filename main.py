from nicegui import ui
import random

# -------------------------
# Game state
# -------------------------
dice = [1, 1, 1, 1, 1]
held = [False] * 5

dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

# -------------------------
# UI references
# -------------------------
dice_buttons = []


# -------------------------
# Game logic
# -------------------------
def roll():
    ui.notify("🎲 Rolling...", position="top", type="info", timeout=0.3)

    for i in range(5):
        if not held[i]:
            dice[i] = random.randint(1, 6)

    update_ui()


def toggle_hold(i: int):
    held[i] = not held[i]
    update_ui()


def reset():
    global dice, held

    dice = [1, 1, 1, 1, 1]
    held = [False] * 5

    update_ui()


# -------------------------
# UI update
# -------------------------
def update_ui():
    for i, btn in enumerate(dice_buttons):
        btn.text = dice_faces[dice[i] - 1]

        if held[i]:
            btn.classes(
                add="border-4 border-red-500 bg-red-100"
            )
            btn.classes(
                remove="bg-blue-100"
            )
        else:
            btn.classes(
                add="bg-blue-100"
            )
            btn.classes(
                remove="border-4 border-red-500 bg-red-100"
            )

# -------------------------
# UI layout
# -------------------------
ui.label("🎲 Lucky Dice").classes("text-2xl font-bold")
#ui.label("Click dice to hold/unhold. Held dice get a red border.").classes("text-gray-600")

with ui.row().classes("gap-2 mt-4"):
    for i in range(5):
        btn = ui.button(
            text="⚀",
            on_click=lambda i=i: toggle_hold(i)
        ).classes(
            "text-5xl w-16 h-16"
        )
        dice_buttons.append(btn)

with ui.row().classes("gap-2 mt-4"):
    ui.button("Roll", on_click=roll).classes("bg-blue-500 text-white px-4 py-2")
    ui.button("Reset", on_click=reset).classes("bg-gray-400 text-white px-4 py-2")

update_ui()

ui.run(host="0.0.0.0", port=8080)