from hub import port
import motor_pair
import runloop

async def main():
    # Set up the drive pair — left motor on A, right motor on B
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Steering = 0 means go perfectly straight
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=400)
    print("Going straight!")
    await runloop.sleep_ms(1000)

    # Steering goes from -100 to 100
    # 0 = straight, 50 = gentle right curve, 100 = spin hard right on the spot
    # Negative numbers turn left: -50 = gentle left, -100 = spin hard left
    motor_pair.move(motor_pair.PAIR_1, 50, velocity=400)
    print("Turning right!")
    await runloop.sleep_ms(1000)

    motor_pair.stop(motor_pair.PAIR_1)
    print("Done turning!")

# Try changing the steering values to 100, -50, or -100 and see what happens!
runloop.run(main())
