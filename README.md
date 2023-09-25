# TOC Project 2022
## Introduction
This is a helper for looking up the **weather**, **air condition**, and **booking ticket**. 

### Loop up for weather and air condition
![](https://i.imgur.com/tk4BqqN.png)
#### Weather:
![](https://i.imgur.com/A1UbKvq.png)
#### Air condition:
![](https://i.imgur.com/gVRCBFe.png)
### Booking tickets
Convinence for people to go on a trip.

![](https://i.imgur.com/Z7UP6RW.png)





## Finite State Machine
![fsm](https://github.com/BaoAh/TOC-LineBot/blob/master/fsm.png?raw=true)

## States
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to weather"
		* Reply: "a list to choose a city for looking up"
	* Input: "go to air"
		* Reply: "a list to choose a city for looking up"
    * Input: "showfsm"
        * Reply: "fsm diagram"
    * Input: "website"
        * Reply: "a list of website"
* weather 
    * Input: "go to weather2"
        * Reply: "goes to weather2"
    * Input: "go back"
        * Reply: "back to user state"
* weather2
    * Input: "go back"
        * Reply: "back to user state"
* air 
    * Input: "go to air"
        * Reply: "goes to air"
    * Input: "go back"
        * Reply: "back to user state"
* air2
    * Input: "go back"
        * Reply: "back to user state"

## Bonus 
- using **web crawler** to get weather information


Flask Architecture ❤️ [@Sirius207](https://github.com/Sirius207)

[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)
