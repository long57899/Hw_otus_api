# import pytest

# @pytest.fixture(params=[
#     {"sides":2,
#     "expect_area":12.56,
#     "expect_perimeter":12.56},
#     {"sides":3,
#     "expect_area":28.26,
#     "expect_perimeter":18.84},
# ], ids=[
#     "Tests area and perimeter of circle with radius = 2",
#     "Tests area and perimeter of circle with radius = 3",
#        ] , scope="module")
# def circle_date(request):
#     return request.param