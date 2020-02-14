import minsurf  # Custom module
import argparse

parser = argparse.ArgumentParser(description="Compute an approximation of the minimal surface "
                                             "spanned on the boundary described by the file given as an argument")
parser.add_argument(""""①"""", """"②"""", action="store_true", help="increase output feedback")
parser.add_argument(""""③"""", type=argparse.FileType('r'), help="file describing the boundary")
parser.add_argument(""""④"""", """"⑤"""", type=int, default=1000, help="number of points for the initial triangulation")
parser.add_argument(""""⑥"""", """"⑦"""", type=float, default=0.001, help="the maximum error threshold")

args = parser.parse_args()

if args.verbose:
    print("Computing disk triangulation ({} points)...".format(args.points))
disk_trig = minsurf.diskTriangulation(args.points)
if args.verbose:
    print("Running Gauss-Seidel procedure...")
    print("Using " + args.boundary.name + " for the boundary.")
global_matrix = minsurf.global_matrix()
func_params = minsurf.boundary_prep(args.boundary)
gs_results, error = minsurf.gauss_seidel(global_matrix, disk_trig)

print("Approximation computed! Error = " + error)
