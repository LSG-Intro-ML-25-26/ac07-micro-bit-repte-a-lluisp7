let player_hand = 0
let hand = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    player_hand = 1
    basic.showIcon(IconNames.SmallSquare)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    player_hand = 3
    basic.showIcon(IconNames.Scissors)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    player_hand = 2
    basic.showIcon(IconNames.Square)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    hand = randint(1, 3)
    basic.clearScreen()
    basic.pause(200)
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
        music.play(music.builtinPlayableSoundEffect(soundExpression.twinkle), music.PlaybackMode.InBackground)
    } else if (hand == 2) {
        basic.showIcon(IconNames.Square)
        music.play(music.tonePlayable(659, music.beat(BeatFraction.Double)), music.PlaybackMode.InBackground)
    } else {
        basic.showIcon(IconNames.Scissors)
        music.play(music.createSoundExpression(WaveShape.Sine, 200, 600, 255, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
    }
    
    basic.pause(1000)
    if (player_hand == hand) {
        basic.showString("DRAW")
    } else if (player_hand == 1 && hand == 3) {
        basic.showString("WIN")
    } else if (player_hand == 2 && hand == 1) {
        basic.showString("WIN")
    } else if (player_hand == 3 && hand == 2) {
        basic.showString("WIN")
    } else {
        basic.showString("LOSE")
    }
    
    player_hand = 0
})
