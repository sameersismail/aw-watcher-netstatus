import argparse
from aw_core.log import setup_logging
from aw_watcher_netstatus.watcher import NetworkWatcher


def main() -> None:
    parser = argparse.ArgumentParser("Monitor network availability.")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="Run with verbose logging.",
    )
    parser.add_argument(
        "--testing", action="store_true", help="Run against test server."
    )
    args = parser.parse_args()

    setup_logging(
        "aw-watcher-netstatus",
        testing=args.testing,
        verbose=args.verbose,
        log_stderr=True,
        log_file=True,
    )

    watcher = NetworkWatcher(testing=args.testing)
    watcher.run()


if __name__ == "__main__":
    main()
