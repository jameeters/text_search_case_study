
class SearchMethod:

    def __init__(self):
        self.target_files = None
        self.pretty_target_filenames = None

    def set_target_files(self, filenames):
        self.target_files = filenames

    def prettyfy(self, results):
        # Get just the actual filename, without a path (but just once)
        if self.pretty_target_filenames is None:
            self.pretty_target_filenames = [name.split('/')[-1] for name in self.target_files]

        pretty_results = dict(zip(self.pretty_target_filenames, results))
        return pretty_results

    def search(self, term):
        raise NotImplementedError

