player_hand = 0
hand = 0

def on_button_pressed_a():
    global player_hand
    player_hand = 1
    basic.show_icon(IconNames.SMALL_SQUARE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global player_hand
    player_hand = 3
    basic.show_icon(IconNames.SCISSORS)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global player_hand
    player_hand = 2
    basic.show_icon(IconNames.SQUARE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global hand, player_hand
    hand = randint(1, 3)
    basic.clear_screen()
    basic.pause(200)
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
        music.play(music.builtin_playable_sound_effect(soundExpression.twinkle),
            music.PlaybackMode.IN_BACKGROUND)
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
        music.play(music.tone_playable(659, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.IN_BACKGROUND)
    else:
        basic.show_icon(IconNames.SCISSORS)
        music.play(music.create_sound_expression(WaveShape.SINE,
                200,
                600,
                255,
                0,
                150,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.IN_BACKGROUND)
    basic.pause(1000)
    if player_hand == hand:
        basic.show_string("DRAW")
    elif player_hand == 1 and hand == 3:
        basic.show_string("WIN")
    elif player_hand == 2 and hand == 1:
        basic.show_string("WIN")
    elif player_hand == 3 and hand == 2:
        basic.show_string("WIN")
    else:
        basic.show_string("LOSE")
    player_hand = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
