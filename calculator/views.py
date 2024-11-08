from django.shortcuts import render

# View to calculate areas
def calculate_area(request):
    if request.method == "POST":
        # Retrieve lists of values for each shape
        lengths = request.POST.getlist("length")
        widths = request.POST.getlist("width")
        bases_triangle = request.POST.getlist("base_triangle")
        heights_triangle = request.POST.getlist("height_triangle")
        bases1_trapezoid = request.POST.getlist("base1_trapezoid")
        bases2_trapezoid = request.POST.getlist("base2_trapezoid")
        heights_trapezoid = request.POST.getlist("height_trapezoid")

        # Initialize lists to store individual areas
        areas_rectangle = []
        areas_triangle = []
        areas_trapezoid = []

        # Helper function to safely convert to float
        def safe_float(value):
            try:
                return float(value)
            except ValueError:
                return 0

        # Calculate areas for each rectangle
        for length, width in zip(lengths, widths):
            if length and width:  # Ensure inputs are not empty
                area = safe_float(length) * safe_float(width)
                areas_rectangle.append(area)

        # Calculate areas for each triangle
        for base, height in zip(bases_triangle, heights_triangle):
            if base and height:  # Ensure inputs are not empty
                area = 0.5 * safe_float(base) * safe_float(height)
                areas_triangle.append(area)

        # Calculate areas for each trapezoid
        for base1, base2, height in zip(bases1_trapezoid, bases2_trapezoid, heights_trapezoid):
            if base1 and base2 and height:  # Ensure inputs are not empty
                area = 0.5 * (safe_float(base1) + safe_float(base2)) * safe_float(height)
                areas_trapezoid.append(area)

        # Calculate total area
        total_area = sum(areas_rectangle) + sum(areas_triangle) + sum(areas_trapezoid)

        # Pass individual areas and total area to the template
        return render(request, "result.html", {
            "areas_rectangle": areas_rectangle,
            "areas_triangle": areas_triangle,
            "areas_trapezoid": areas_trapezoid,
            "total_area": total_area,
            "square_feet": total_area *10.76
        })

    return render(request, "index.html")
