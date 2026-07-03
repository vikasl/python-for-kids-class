# Import the light_matrix so we can control the 5x5 LED display on the hub
from hub import light_matrix
# Import runloop so we can use sleep_ms() for waiting
import runloop

# Every SPIKE Prime 3 program puts its code inside an async function called main()
# "async" means the robot can do precise timing with "await"
async def main():
   
    
    light_matrix.show_image(light_matrix.IMAGE_ASLEEP)

    await runloop.sleep_ms(1000)

    light_matrix.clear()

    light_matrix.show_image(light_matrix.IMAGE_HEART)

    await runloop.sleep_ms(1000)

    light_matrix.clear()

    light_matrix.show_image(light_matrix.IMAGE_DUCK)

    await runloop.sleep_ms(1000)

    light_matrix.clear()

    light_matrix.write("Everyone is better than Devansh Aggarwal")
    
    
runloop.run(main())