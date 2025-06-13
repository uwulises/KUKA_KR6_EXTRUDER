from patterns.translate_KRL import KRLTranslator
from stl_to_path import slice_stl_perimeters, extract_positions_from_slices

slices = slice_stl_perimeters("example.stl", slice_height=1.6)

positions = extract_positions_from_slices(slices, slice_height=1.6)

positions = [(x + 1200, y, z + 700) for x, y, z in positions]

filename_export = "example_path"

krl = KRLTranslator(filename_export, axis_vel=[
                    15, 15, 15, 15, 15, 15], speed_ms=0.03)
krl.create_KRL_file()
krl.add_line_to_src_file("; USER POSES CALLS \n")
# TODO: Call the first pose from setup config and save a new json file with the new starting pose
krl.add_line_to_src_file("PTP {X 750, Y 300, Z 1200, A -180, B 55, C -180} \n")
krl.add_line_to_src_file("WAIT SEC 5 \n")
krl.add_line_to_src_file("; USER POSES CALLS \n")
for pose in positions:
    krl.add_line_to_src_file("LIN {X " + str(pose[0]) + ", Y " + str(pose[1]) + ", Z " + str(
        pose[2]) + ", A " + str(0) + ", B " + str(90) + ", C " + str(0) + "}\n")
krl.add_line_to_src_file("\n")
krl.add_line_to_src_file(";Wait for \n")
krl.add_line_to_src_file(krl.sleep(5))
krl.add_line_to_src_file("; END POSITION FOR \n")