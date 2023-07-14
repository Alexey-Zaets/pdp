class DataPipeline:

    def __inti__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path

    def extract_data(self) -> dict:
        ...

    def transform_data(self, data: dict) -> dict:
        ...

    def save_data(self, data: dict) -> None:
        ...
