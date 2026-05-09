game.startCountdown(15000)
let Score = 0
let Dot_x = 2
let Dot_y = 2
let Player_x = 0
let Player_y = 0
led.plot(Dot_x, Dot_y)
basic.forever(function () {
    if (input.isGesture(Gesture.TiltRight) && Player_x < 4) {
        led.toggle(Player_x, Player_y)
        Player_x += 1
    } else if (input.isGesture(Gesture.LogoUp) && Player_y < 4) {
        led.toggle(Player_x, Player_y)
        Player_y += 1
    } else if (input.isGesture(Gesture.TiltLeft) && Player_x > 0) {
        led.toggle(Player_x, Player_y)
        Player_x += -1
    } else if (input.isGesture(Gesture.LogoDown) && Player_y > 0) {
        led.toggle(Player_x, Player_y)
        Player_y += -1
        basic.pause(150)
    }
})
basic.forever(function () {
    if (Player_x == Dot_x && Player_y == Dot_y) {
        led.toggle(Dot_x, Dot_y)
        Score += 1
        Dot_x = randint(0, 4)
        Dot_y = randint(0, 4)
        led.toggle(Dot_x, Dot_y)
    } else if (game.isGameOver()) {
        game.gameOver()
    } else {
        led.plot(Player_x, Player_y)
    }
})
