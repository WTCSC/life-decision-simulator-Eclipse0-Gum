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

![Life Decision Simulator Demo](/home/mendozac@CSGP.EDU/life-decision-simulator-Eclipse0-Gum/Decision_Test.gif)

 # [Start: wake_up_scene]
        |
        V
  "Get up" ------------------------------> [bag_scene]
   |                                              |
   |                                              V
 "Sleep"                                      "Open Bag" ---> [Game Over]
   |                                                 |
 [Game Over]                                   "Leave Bag"
                                                     |
                                                     |
                                               [run_scene]
                                                     |
                                   +-----------------+-----------------+ 
                                   |                                   |
                              "Run" --> [Game Over]               "Sandal"
                                                                        |
                                                                        v
                                                                  [voice_scene]
                                                                         |
                                                         +---------------+----------------+
                                                         |                                |
                                                   "Accept" or "Decline"        (Both same outcome)
                                                        |                                
                                                        V
                                                     [final_scene]
                                                     |
                                 +-------------------+-------------------+
                                 |                                       |
                            "Forfeit Offer"                            "Accept Offer"
                                 |                                       |
                                 v                                       v
                                [Game Over]                [Ascend → Twist ending with Dr. House]