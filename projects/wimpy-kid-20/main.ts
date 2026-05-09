input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showString("Not again, Mom!")
    basic.showLeds(`
        . # . # .
        . # . # .
        . . # . .
        # . . . #
        . # # # .
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    basic.showString("Rodrick rules")
    basic.showLeds(`
        . # . # .
        . # . # .
        . . # . .
        # . . . #
        . # # # .
        `)
})
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    basic.showIcon(IconNames.Surprised)
    basic.showLeds(`
        . # . # .
        . # . # .
        . . # . .
        # . . . #
        . # # # .
        `)
})
basic.showLeds(`
    . # . # .
    . # . # .
    . . # . .
    # . . . #
    . # # # .
    `)
