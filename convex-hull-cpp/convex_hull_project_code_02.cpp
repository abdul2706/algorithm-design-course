#include <ctime>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>

#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/convex_hull_2.h>
#include <CGAL/Convex_hull_traits_adapter_2.h>
#include <CGAL/property_map.h>
#include <vector>
#include <numeric>

using namespace std;

typedef CGAL::Exact_predicates_inexact_constructions_kernel K;
typedef K::Point_2 Point_2;
typedef CGAL::Convex_hull_traits_adapter_2<K, CGAL::Pointer_property_map<Point_2>::type > Convex_hull_traits_2;

int generate_random_within(int start, int end);
void print_points(int *points, int rows, int cols);

int main() {
    // define required variables
    int MAX_POINTS = 10000000;
    int STEP_SIZE = 50000;
    int dimensions = 2;
    int x_limit_start = 0, x_limit_end = 200000000;
    int y_limit_start = 0, y_limit_end = 200000000;
    int z_limit_start = 0, z_limit_end = 200000000;
    int *points_array;
    clock_t start, end;
    double cpu_time;

    // open log file for saving input vs time per algorithm run
    ofstream log_file_pointer;
    log_file_pointer.open("convex-hull-" + to_string(MAX_POINTS) + "-" + to_string(STEP_SIZE) + ".csv");
    log_file_pointer << "n, cpu_time" << endl;

    // loop over all files generated in part-a
    for (int total_points = 0; total_points <= MAX_POINTS; total_points += STEP_SIZE) {
        points_array = (int *)malloc((total_points * dimensions) * sizeof(int));

        for (int i = 1; i <= total_points; i++) {
            points_array[i * dimensions + 0] = generate_random_within(x_limit_start, x_limit_end);
            points_array[i * dimensions + 1] = generate_random_within(y_limit_start, y_limit_end);
        }

        vector<Point_2> points;
        for (int i = 0; i < total_points; i++) {
            points.push_back(Point_2(points_array[i * dimensions + 0], points_array[i * dimensions + 1]));
        }
        vector<size_t> indices(points.size()), out;
        iota(indices.begin(), indices.end(), 0);

        // apply algorithm and note time taken
        start = clock();
        CGAL::convex_hull_2(
            indices.begin(), 
            indices.end(), 
            back_inserter(out), 
            Convex_hull_traits_2(CGAL::make_property_map(points))
        );
        end = clock();

        // take time difference and save the logs
        cpu_time = ((double)(end - start)) / CLOCKS_PER_SEC;
        cout << "Time Taken by " << total_points << " points = " << cpu_time << endl;
        log_file_pointer << total_points << ", " << cpu_time << endl;
        
        free(points_array);
    }

    log_file_pointer.close();
    cout << "Program End..." << endl;
    return 0;
}

int generate_random_within(int start, int end) {
    float number_generated = (float)rand() / RAND_MAX;
    return (int)(number_generated * (end - start + 1)) + start;
}

void print_points(int *points, int rows, int cols) {
    cout << "x, y";
    if (cols == 3) {
        cout << ", z";
    }
    cout << endl;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << points[i * cols + j];
            if (j < cols - 1) {
                cout << ", ";
            }
        }
        cout << endl;
    }
}
