class SearchMethod:
    def __init__(self):
        self.target_files = None
        self.pretty_target_filenames = None

    def set_target_files(self, filenames):
        self.target_files = filenames

    def prettyfy_results(self, results):
        # Get just the actual filename, without a path (but just once)
        if self.pretty_target_filenames is None:
            self.pretty_target_filenames = [name.split('/')[-1] for name in self.target_files]

        # Results ordered from greatest to least, but with the format [(result, name)...]
        pairs = sorted([(results[i], self.pretty_target_filenames[i]) for i, _ in enumerate(results)], reverse=True)
        # Reverse each tuple
        pairs = [p[::-1] for p in pairs]
        return pairs



    def search(self, term):
        raise NotImplementedError
