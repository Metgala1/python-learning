class ResourceManager:
    def __init__(self, resource_name, should_fail=False):
        self.resource_name = resource_name
        self.should_fail = should_fail
        self.state = "closed"

    def __enter__(self):
        if self.state != "closed":
            raise RuntimeError("Resource is already active")

        try:
            self.state = "opening"

            print(f"Opening: {self.resource_name}")

            self.state = "open"

            print("Configuring resource...")

            if self.should_fail:
                raise RuntimeError("Configuration failed")

            self.state = "ready"

            print("Resource successfully configured")

            return self

        except Exception:
            print("Acquisition failed. Cleaning up...")
            self.state = "closed"
            raise

    def use_resource(self):
        if self.state != "ready":
            raise RuntimeError("Resource is not ready")

        print(f"Using: {self.resource_name}")

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if exc_type is not None:
                print(f"An error occurred: {exc_value}")
            else:
                print("Resource operation completed successfully")

            print(f"Releasing: {self.resource_name}")

        finally:
            self.state = "closed"

        return False

resource = ResourceManager("Database connection")

try:
    with resource:
        resource.use_resource()
        raise ValueError("Database operation failed")

except ValueError as error:
    print("Caught:", error)

print("Final state:", resource.state)