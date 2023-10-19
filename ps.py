


try:
    while True:
        spo2_data = get_sensor_data("spo2")
        heart_rate_data = get_sensor_data("heartrate")
        temp_data = get_sensor_data("temperature")

        if spo2_data is not None:
            print(f"SPO2: {spo2_data}")

        if heart_rate_data is not None:
            print(f"Heart Rate: {heart_rate_data}")

        if temp_data is not None:
            print(f"Temperature C: {temp_data}")
            print("")

        # Add a delay before the next request (e.g., 5 seconds)
        time.sleep(2)

        # Check for user input (non-blocking)
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.read(1)
            if key == "q":
                break

except KeyboardInterrupt:
    print("Script stopped by user (Ctrl+C)")
