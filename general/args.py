""" Parse aruments """

import argparse

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--string',
        type=str,
        default="default/value/to/string",
        help='Set string value')
    parser.add_argument(
        '--true',
        default=True,
        action="store_false",
        help='Toggle flag having default value to True')
    parser.add_argument(
        '--false',
        default=False,
        action="store_true",
        help='Toggle flag having default value to False')
    parser.add_argument(
        '--int',
        default=99,
        help='Set integer value')
    parser.add_argument(
        '--list',
        default=[71, 99],
        # Use nargs='+' if you want to receive any number
        nargs=2,
        help='Pass a list (upto 2) of integers')

    # Use can specified verbose multiple times so just count
    # how many this parameter bas been specified
    parser.add_argument('--verbose', 
            action='count', 
            default=0,
            help='Set verbose level (can specify it multiple timess)')

    # Input should be with in the specified range
    parser.add_argument('--irange', type=int, choices=range(5, 9))

    # Input should be from the choices we have specified
    parser.add_argument('--ichoice', type=int, choices=[10,20,30])

    # Setup mutual exclusive parameters
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--option1", action="store_true")
    group.add_argument("--option2", action="store_true")

    # Show version
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0")

    args_known, args_unknown = parser.parse_known_args()
    print(f"-------------------------------")
    print(f"Param # string:     {args_known.string}")
    print(f"Param # true:       {args_known.true}")
    print(f"Param # false:      {args_known.false}")
    print(f"Param # int:        {args_known.int}")
    print(f"Param # list:       {args_known.list}")
    print(f"Param # verbose:    {args_known.verbose}")
    print(f"Param # irange:     {args_known.irange}")
    print(f"Param # ichoice:    {args_known.ichoice}")
    print(f"Param # option1:    {args_known.option1}")
    print(f"Param # option2:    {args_known.option2}")
    print(f"-------------------------------")
