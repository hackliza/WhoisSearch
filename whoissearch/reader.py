from typing import Any, Iterator, Optional


class Reader:
    def read_white_list(self, targets: Any):
        return list(self.read_text_targets(targets))

    def read_black_list(self, targets: Any):
        if targets is not None:
            return list(self.read_text_targets(targets))
        return None

    def read_text_targets(self, targets: Any) -> Iterator[str]:
        yield from self.read_text_lines(self.read_targets(targets))

    def read_targets(self, targets: Optional[Any]) -> Iterator[str]:
        """Function to process the program ouput that allows to read an array
        of strings or lines of a file in a standard way. In case nothing is
        provided, input will be taken from stdin.
        """

        for target in targets:
            try:
                with open(target) as fi:
                    yield from fi
            except FileNotFoundError:
                yield target

    def read_text_lines(self, fd: Iterator[str]) -> Iterator[str]:
        """To read lines from a file and skip empty lines or those commented
        (starting by #)
        """
        for line in fd:
            line = line.strip()
            if line == "":
                continue
            if line.startswith("#"):
                continue

            yield line
