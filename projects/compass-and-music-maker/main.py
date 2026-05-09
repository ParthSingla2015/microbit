def on_pin_released_p2():
    basic.show_string("Hello from Parth")
input.on_pin_released(TouchPin.P2, on_pin_released_p2)

def on_pin_released_p0():
    basic.show_string("Music mode on")
input.on_pin_released(TouchPin.P0, on_pin_released_p0)

def on_logo_long_pressed():
    music.play(music.string_playable("C5 A B G A F G E ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    music.play(music.string_playable("C D E F G A B C5 ", 500),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 B A G F E D C ", 500),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_free_fall():
    music.play(music.string_playable("C A G E G F D B ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

def on_gesture_tilt_left():
    music.play(music.string_playable("C5 B A - C5 B A - ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_screen_up():
    music.play(music.string_playable("E D G F B A C5 B ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_screen_down():
    music.play(music.string_playable("C5 G B A F A C5 B ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_ab():
    music.play(music.string_playable("C D E - D E F - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("E F G - F G A C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("G A B - A B C5 - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 B A - B A G - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("A G F - G F E - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("F E D - E D C - ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.play(music.string_playable("C C D D E E F F ", 500),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("G G A A B B C5 C5 ", 500),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 C5 B B A A G G ", 500),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("F F E E D D C C ", 500),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    music.play(music.string_playable("B A G A G F A C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    music.play(music.string_playable("G A B - G A B - ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    music.play(music.string_playable("G F G A - F E D ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_logo_touched():
    music.play(music.string_playable("A F E F D G E F ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_pin_released_p1():
    basic.show_string("Creative coding time")
input.on_pin_released(TouchPin.P1, on_pin_released_p1)

def on_logo_pressed():
    music.play(music.string_playable("E B C5 A B G A F ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

degrees = 0
basic.show_string("Hello this is a compass and a music maker by Parth")

def on_forever():
    global degrees
    degrees = input.compass_heading()
    if degrees < 45 or degrees > 315:
        basic.show_leds("""
            . . # . .
            . # # # .
            . . # . .
            . . # . .
            . . # . .
            """)
    elif degrees < 135:
        basic.show_leds("""
            . . . . .
            . # . . .
            # # # # #
            . # . . .
            . . . . .
            """)
    elif degrees < 225:
        basic.show_leds("""
            . . # . .
            . . # . .
            . . # . .
            . # # # .
            . . # . .
            """)
    else:
        basic.show_leds("""
            . . . . .
            . . . # .
            # # # # #
            . . . # .
            . . . . .
            """)
basic.forever(on_forever)
