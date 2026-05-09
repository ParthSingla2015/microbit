input.onButtonPressed(Button.A, function () {
    if (Cond == 1) {
        Answer = "" + Answer + "A"
        Check()
    } else {
        game.gameOver()
    }
})
function Check () {
    if (Answer.length == Length) {
        if (Answer == Question) {
            basic.showLeds(`
                . . . . #
                . . . # .
                # . # . .
                . # . . .
                . . . . .
                `)
            game.addScore(1)
            basic.pause(500)
            Generate()
        } else {
            basic.showLeds(`
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                `)
            game.gameOver()
        }
    }
}
input.onButtonPressed(Button.AB, function () {
    Generate()
})
input.onButtonPressed(Button.B, function () {
    if (Cond == 1) {
        Answer = "" + Answer + "B"
        Check()
    } else {
        game.gameOver()
    }
})
function Generate () {
    basic.showLeds(`
        # # # # #
        # . . . #
        # . # . #
        # . . . #
        # # # # #
        `)
    basic.pause(50)
    Answer = ""
    Question = ""
    Length = 2 + (Level - 1) * 2
    Cond = 1
    for (let index = 0; index < Length; index++) {
        RandNum = randint(1, 2)
        Cond = 0
        if (RandNum == 1) {
            AB = "A"
        } else {
            AB = "B"
        }
        if (game.isGameOver()) {
            break;
        }
        basic.showString(AB)
        basic.pause(Delay)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        Question = "" + Question + AB
    }
    if (!(game.isGameOver())) {
        Level += 1
        if (Delay >= 50) {
            Delay += -50
        }
        Cond = 1
        basic.showString("?")
    }
}
let AB = ""
let RandNum = 0
let Question = ""
let Length = 0
let Answer = ""
let Cond = 0
let Delay = 0
let Level = 0
led.setBrightness(25)
basic.showLeds(`
    . . . . .
    . # . # .
    # # . # #
    . # . # .
    . . . . .
    `)
Level = 1
Delay = 500
game.setScore(0)
