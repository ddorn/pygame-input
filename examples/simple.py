"""
This is a simple example to demonstrate
how to use pygame_inputs to easily register callbacks
on pygame events.
"""
import pygame

from pygame_input import Inputs, QuitEvent, Button, Axis


def main():
    screen = pygame.display.set_mode((800, 500))

    inputs = Inputs()
    inputs["quit"] = Button(QuitEvent(), pygame.K_q)
    inputs["invert"] = Button(pygame.K_RETURN, pygame.K_SPACE)
    inputs["axis"] = Axis(pygame.K_LEFT, pygame.K_RIGHT)

    color = [255, 165, 0]

    def invert(_):
        print("Inverted !")
        for i in range(3):
            color[i] = 255 - color[i]

    def set_blue(axis: Axis):
        # Here we just map the axis value from [-1, 1]
        # to [0, 255]
        color[2] = int(127.5 * (axis.value + 1))

    # Here we add the callback at the same place we define inputs
    # But it doesn't have to be that case, see more_complex.py for
    # more details.
    # Also ours functions are modifying a global state, but usually
    # you would pass bound functions like `myapp.invert_background`
    # when working  with classes.

    # Notice: we pass the function without calling it
    inputs["invert"].on_press_repeated(invert, 0.3)
    inputs["axis"].always_call(set_blue)
    # The first parameter of a callback is always the Button/Axis
    # But we don't need it here and dont want to pass it to quit()
    inputs["quit"].on_press(lambda _: quit())

    clock = pygame.time.Clock()
    while True:
        # Converting the event to a list is important
        # Otherwise we can only iterate them once
        events = list(pygame.event.get())
        inputs.trigger(events)

        screen.fill(color)
        pygame.display.update()

        clock.tick(60)


if __name__ == "__main__":
    main()
