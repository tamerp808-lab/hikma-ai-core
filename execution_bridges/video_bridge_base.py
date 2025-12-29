class VideoExecutionBridge:
    """
    Base interface for any video generation engine
    """

    def execute_scene(self, scene: dict):
        raise NotImplementedError("Video engine not connected yet")
