# Life Decision Simulator  

The **Life Decision Simulator** is an interactive program where players make choices that affect their virtual lives. Each decision creates unique outcomes but stuck to a limited path. 

---

## Features  
- Multiple decision paths with different outcomes  
- Limited Events 
- Simple, text-based interface  
- Educational tool for learning decision-making purposes 

---

## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/WTCSC/life-decision-simulator-Eclipse0-Gum
   cd life-decision-simulator-Eclipse0-Gum



![Status](https://img.shields.io/badge/status-working-brightgreen)
![Python](https://img.shields.io/badge/made%20with-Python-blue)


## Demo  

Here’s a quick demo of the Life Decision Simulator in action:  

![Life Decision Simulator Demo](media/Decision_Test.gif)

                                START GAME
CALL wake_up_scene

FUNCTION wake_up_scene:
    PRINT dramatic intro (waking up in apocalypse)
    ASK: "Do you get up or sleep?"
    IF choice == "sleep":
        GAME OVER (dog kills you)
    ELSE:
        CALL bag_scene

FUNCTION bag_scene:
    PRINT story about finding a bag
    ASK: "Do you open or leave?"
    IF choice == "open":
        PRINT sucked into world → explosion
        GAME OVER
    ELSE:
        CALL run_scene

FUNCTION run_scene:
    PRINT story about survivors, statue of mom, sandal
    ASK: "Sandal or run?"
    IF choice == "run":
        GAME OVER (beaten to death)
    ELSE:
        CALL voice_scene

FUNCTION voice_scene:
    PRINT sandal powers + mysterious voice
    ASK: "Accept or decline?"
    (Both lead to same outcome → horde attacks)
    CALL final_scene

FUNCTION final_scene:
    PRINT horde + final choice
    ASK: "Accept offer or forfeit offer?"
    IF choice == "forfeit offer":
        GAME OVER (evaporated by horde)
    ELSE IF choice == "accept offer":
        PRINT gain powers, kill horde, ascend
        END (twist ending with Dr. House)

FUNCTION game_over(message):
    PRINT GAME OVER message
    EXIT