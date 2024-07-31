#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

double sum_array(py::array_t<double> input) {
    py::buffer_info buf = input.request();
    double* ptr = static_cast<double*>(buf.ptr);
    size_t size = buf.size;

    double sum = 0.0;
    for (size_t i = 0; i < size; i++) {
        sum += ptr[i];
    }

    return sum;
}

PYBIND11_MODULE(sum_array, m) {
    m.def("sum_array", &sum_array, "Sum all elements in a NumPy array");
}
