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

        # The indices of the entries in results, from highest to lowest
        # (I.e. the first entry is the index of the largest entry.)
        order = [t[0] for t in sorted(enumerate(results))]
        pretty_results = [(self.pretty_target_filenames[i], results[i]) for i in order]
        return pretty_results


    def search(self, term):
        raise NotImplementedError
