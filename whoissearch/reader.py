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
        for target in targets:
            try:
                with open(target) as fi:
                    yield from fi
            except FileNotFoundError:
                yield target

    def read_text_lines(self, fd: Iterator[str]) -> Iterator[str]:
        for line in fd:
            line = line.strip()
            if line == "":
                continue
            if line.startswith("#"):
                continue

            yield line
