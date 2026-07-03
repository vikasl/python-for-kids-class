# Import the light_matrix so we can control the 5x5 LED display on the hub
from hub import light_matrix
# Import runloop so we can use sleep_ms() for waiting
import runloop

# Every SPIKE Prime 3 program puts its code inside an async function called main()
# "async" means the robot can do precise timing with "await"
async def main():
    # Show a built-in happy face image on the display
    # All image names start with light_matrix.IMAGE_
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)

    # Wait 2 seconds (2000 milliseconds) so we can see the image
    # Always use "await" before runloop.sleep_ms()
    await runloop.sleep_ms(2000)

    # Turn off all 25 LEDs
    light_matrix.clear()

    # Send a message to the computer screen
    print("Hello from your SPIKE Prime robot!")

# This line actually starts your program — always put it at the very end!
runloop.run(main())
