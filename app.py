from flask import Flask, render_template, request
from fractions import Fraction

app = Flask(__name__)


def tail_width(
    board_width: Fraction,
    number_tails: Fraction,
    half_pin_size: Fraction,
    pin_size: Fraction,
) -> Fraction:
    """
    Function to calculate width of tail, given some inputs.

    Args:
        board_width (Fraction): width of board receiving dovetails.
        number_tails (Fraction): number of tails to be cut.
        half_pin_size (Fraction): width of half-pins (pins on edge of board).
        pin_size (Fraction): width of intermediate pins.

    Returns:
        (Fraction): width of tail.
    """
    return (board_width - 2 * half_pin_size + pin_size) / number_tails - pin_size


@app.route("/form")
def form():
    """
    Function to render input form on /form route
    """
    return render_template("form.html")


@app.route("/data", methods=["POST", "GET"])
def data():
    """
    Function to compute tail-width and post data to /data route.
    """
    if request.method == "GET":
        return (
            f"The URL /data is accessed directly. Try going to '/form' to submit form"
        )

    if request.method == "POST":

        # Get data
        form_data = request.form

        number_tails = Fraction(form_data["number_tails"])
        board_width = Fraction(form_data["board_width"])
        half_pin_size = Fraction(form_data["half_pin_size"])
        pin_size = Fraction(form_data["pin_size"])

        tail_size = tail_width(board_width, number_tails, half_pin_size, pin_size)

        print(
            "\nTail Width: ",
            tail_size,
            "in ~ ",
            round(float(tail_size) * 25.4, 1),
            " mm",
        )

        max_denominator = max(
            8,
            min(
                32,
                max(
                    tail_size.denominator,
                    board_width.denominator,
                    half_pin_size.denominator,
                    pin_size.denominator,
                ),
            ),
        )

        # Forming dovetail layout string
        half_pin_string = "_" * int(
            half_pin_size.numerator * max_denominator / half_pin_size.denominator
        )
        pin_string = "_" * int(
            pin_size.numerator * max_denominator / pin_size.denominator
        )
        tail_string = (
            "\\"
            + "_" * int(tail_size.numerator * max_denominator / tail_size.denominator)
            + "/"
        )

        string = (
            "|"
            + half_pin_string
            + int(number_tails - 1) * (tail_string + pin_string)
            + tail_string
            + half_pin_string
            + "|"
        )

        print()
        print("_" * len(string))
        print(string)

        # rendering data template
        return render_template(
            "data.html",
            form_data={
                "Half-Pins": {
                    "in Fractional Inches": half_pin_size,
                    "in Decimal Inches": float(half_pin_size),
                    "in Millimeters": round(float(half_pin_size) * 25.4, 2),
                },
                "Pins": {
                    "in Fractional Inches": pin_size,
                    "in Decimal Inches": float(pin_size),
                    "in Millimeters": round(float(pin_size) * 25.4, 2),
                },
                "Tails": {
                    "Count": number_tails,
                    "in Fractional Inches": tail_size,
                    "in Decimal Inches": round(float(tail_size), 3),
                    "in Millimeters": round(float(tail_size) * 25.4, 2),
                },
                "Shape": {"Layout": string},
            },
        )


if __name__ == "__main__":
    app.run(debug=False)
