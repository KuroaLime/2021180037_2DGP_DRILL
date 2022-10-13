import pico2d
import play_state
import logo_state

start_state = logo_state

pico2d.open_canvas()

states=[logo_state, play_state] #list안에는 별게 다 들어간다.

for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()

# finalization code

pico2d.close_canvas()
