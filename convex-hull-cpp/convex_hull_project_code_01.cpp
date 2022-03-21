// #include <ctime>
// #include <string>
// #include <fstream>
// #include <iostream>

// #include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
// #include <CGAL/convex_hull_2.h>
// #include <CGAL/Convex_hull_traits_adapter_2.h>
// #include <CGAL/property_map.h>
// #include <vector>
// #include <numeric>

// using namespace std;

// typedef CGAL::Exact_predicates_inexact_constructions_kernel K;
// typedef K::Point_2 Point_2;
// typedef CGAL::Convex_hull_traits_adapter_2<K, CGAL::Pointer_property_map<Point_2>::type > Convex_hull_traits_2;

// int generate_random_within(int start, int end);
// void print_points(int *points, int rows, int cols);

// int main() {
//     int total_points = 1000, dimensions = 2;
//     int x_limit_start = 0, x_limit_end = 1000000;
//     int y_limit_start = 0, y_limit_end = 1000000;
//     int z_limit_start = 0, z_limit_end = 1000000;
//     int *points_array = (int *)malloc((total_points * dimensions) * sizeof(int));

//     for (int i = 1; i <= total_points; i++) {
//         points_array[i * dimensions + 0] = generate_random_within(x_limit_start, x_limit_end);
//         points_array[i * dimensions + 1] = generate_random_within(y_limit_start, y_limit_end);
//     }

//     vector<Point_2> points;
//     for (int i = 0; i < total_points; i++) {
//         points.push_back(Point_2(points_array[i * dimensions + 0], points_array[i * dimensions + 1]));
//     }
//     cout << "[points.size()] -> " << points.size() << endl;

//     vector<size_t> indices(points.size()), out;
//     cout << "[indices] -> " << indices.size() << endl;
    
//     iota(indices.begin(), indices.end(), 0);
//     CGAL::convex_hull_2(
//         indices.begin(), 
//         indices.end(), 
//         back_inserter(out), 
//         Convex_hull_traits_2(CGAL::make_property_map(points))
//     );
//     for( size_t i : out ) {
//         cout << "points[" << i << "] = " << points[i] << endl;
//     }



//     // clock_t start, end;
//     // double cpu_time;
//     // ofstream log_file_pointer;
//     // log_file_pointer.open("log-merge-sort.csv");
//     // if (log_file_pointer == NULL) {
//     //     cout << "Failed to open log file, try again.";
//     //     exit(0);
//     // }
//     // // write header in log file
//     // log_file_pointer << "n, cpu_time" << endl;

//     // // loop over all files generated in part-a
//     // for (int i = 1; i < total_points; i++) {
//     //     // apply algorithm and note time taken
//     //     start = clock();
    
//     //     std::vector<Point_2> points = { Point_2(10,0),
//     //                                     Point_2(10,0),
//     //                                     Point_2(0,10),
//     //                                     Point_2(1,1),
//     //                                     Point_2(3,4),
//     //                                     Point_2(0,0),
//     //                                     Point_2(10,10),
//     //                                     Point_2(2,6) };
//     //     cout << "[points.size()] -> " << points.size() << endl;

//     //     std::vector<std::size_t> indices(points.size()), out;
//     //     std::iota(indices.begin(), indices.end(), 0);
//     //     CGAL::convex_hull_2(
//     //         indices.begin(), 
//     //         indices.end(), 
//     //         std::back_inserter(out), 
//     //         Convex_hull_traits_2(CGAL::make_property_map(points))
//     //     );
//     //     for( std::size_t i : out ) {
//     //         std::cout << "points[" << i << "] = " << points[i] << std::endl;
//     //     }

//     //     end = clock();

//     //     // take time difference and save the logs
//     //     cpu_time = ((double)(end - start)) / CLOCKS_PER_SEC;
//     //     cout << "Time Taken by " << i << " points = " << cpu_time << endl;
//     //     log_file_pointer << i << ", " << cpu_time << endl;
//     // }

//     // free(points_array);
//     // log_file_pointer.close();

//     // cout << "(Press Enter key to close the program...)" << endl;
//     // getchar();
//     // return 0;
//     cout << "[Hello World] program ends" << endl;
//     return 0;
// }

// int generate_random_within(int start, int end) {
//     float number_generated = (float)rand() / RAND_MAX;
//     return (int)(number_generated * (end - start + 1)) + start;
// }

// void print_points(int *points, int rows, int cols) {
//     cout << "x, y";
//     if (cols == 3) {
//         cout << ", z";
//     }
//     cout << endl;
//     for (int i = 0; i < rows; i++) {
//         for (int j = 0; j < cols; j++) {
//             cout << points[i * cols + j];
//             if (j < cols - 1) {
//                 cout << ", ";
//             }
//         }
//         cout << endl;
//     }
// }
