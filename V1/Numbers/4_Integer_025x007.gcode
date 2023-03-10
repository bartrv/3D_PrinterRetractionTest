; generated by PrusaSlicer 2.4.0+win64 on 2022-05-06 at 21:27:38 UTC

; 

; external perimeters extrusion width = 0.25mm
; perimeters extrusion width = 0.25mm
; infill extrusion width = 0.50mm
; solid infill extrusion width = 0.25mm
; top infill extrusion width = 0.25mm
; first layer extrusion width = 0.25mm

M73 P0 R2
M73 Q0 S2
M201 X800 Y800 Z200 E4000 ; sets maximum accelerations, mm/sec^2
M203 X200 Y200 Z12 E120 ; sets maximum feedrates, mm/sec
M204 P800 R800 T800 ; sets acceleration (P, T) and retract acceleration (R), mm/sec^2
M205 X6.00 Y6.00 Z0.40 E4.50 ; sets the jerk limits, mm/sec
M205 S0 T0 ; sets the minimum extruding and travel feed rate, mm/sec
M107
;TYPE:Custom
M862.3 P "MK3SMMU2S" ; printer model check
M862.1 P0.25 ; nozzle diameter check
M115 U3.9.1 ; tell printer latest fw version
G90 ; use absolute coordinates
M83 ; extruder relative mode
M104 S210 ; set extruder temp
M140 S60 ; set bed temp
M190 S60 ; wait for bed temp
M109 S210 ; wait for extruder temp
G28 W ; home all without mesh bed level
G80 ; mesh bed leveling

;Skelestruder Code Start - Currently managed by custom Firmware
;M350 E16 ; 16 Microsteps instead of 32
;M92 E492 ; 492 steps/mm instead of 280  Flow Test result was 492
;M221 S95 ; Set flow to tested Stable 95%
;Skelestruder Code End

; Send the filament type to the MMU2.0 unit.
; E stands for extruder number, F stands for filament type (0: default; 1:flex; 2: PVA)
M403 E0 F0
M403 E1 F0
M403 E2 F0
M403 E3 F0
M403 E4 F0


;go outside print area
G1 Y-3.0 F1000.0
G1 Z0.4 F1000.0
; select extruder
T0
; initial load
G1 X55.0 E29.0 F1073.0
G1 X5.0 E15.0 F1800.0
M73 P2 R2
M73 Q2 S2
G1 X55.0 E8.0 F2000.0
M73 P3 R2
M73 Q3 S2
G1 Z0.3 F1000.0
G92 E0.0
M73 P5 R2
M73 Q5 S2
G1 X240.0 E25.0 F2200.0
G1 Y-2.0 F1000.0
M73 P9 R1
M73 Q9 S1
G1 X55.0 E25 F1400.0
G1 Z0.20 F1000.0
M73 P15 R1
M73 Q15 S1
G1 X5.0 E4.0 F1000.0
G92 E0.0


;M221 S100
G92 E0.0

; Don't change E values below. Excessive value can damage the printer.

G21 ; set units to millimeters
G90 ; use absolute coordinates
M83 ; use relative distances for extrusion
M900 K0
M107
;LAYER_CHANGE
;Z:0.15
;HEIGHT:0.15
;BEFORE_LAYER_CHANGE
G92 E0.0
;0.15


G1 E-.6 F1800
M73 P17 R1
M73 Q17 S1
G1 Z.15 F10800
;AFTER_LAYER_CHANGE
;0.15
G1 X29.485 Y29.679
G1 E.6 F1800
M204 S500
;TYPE:External perimeter
;WIDTH:0.25
M73 P18 R1
M73 Q18 S1
G1 F900
G1 X30.32 Y29.679 E.01134
G1 X30.32 Y30.545 E.01176
G1 X30.067 Y30.617 E.00357
G1 X29.505 Y29.711 E.01448
M204 S800
G1 X29.422 Y29.437 F10800
G1 E-.6 F1800
G1 X30.462 Y28.899 F10800
G1 E.6 F1800
M204 S500
G1 F900
G1 X30.462 Y29.537 E.00867
G1 X30.657 Y29.537 E.00265
G1 X30.657 Y29.679 E.00193
G1 X30.462 Y29.679 E.00265
G1 X30.462 Y31.243 E.02124
G1 X30.264 Y31.243 E.00269
G1 X29.343 Y29.768 E.02362
M73 Q19 S1
G1 X29.343 Y29.537 E.00314
M73 P19 R1
G1 X30.32 Y29.537 E.01327
G1 X30.32 Y28.899 E.00867
G1 X30.124 Y28.899 E.00265
G1 X30.124 Y28.757 E.00193
G1 X30.657 Y28.757 E.00723
G1 X30.657 Y28.899 E.00193
G1 X30.499 Y28.899 E.00214
M204 S800
G1 X30.217 Y28.951 F10800
G1 E-.6 F1800
M107
;TYPE:Custom
; Filament-specific end gcode

G1 X0 Y210 F7200
G1 E2 F5000
M73 P20 R1
M73 Q20 S1
G1 E2 F5500
M73 Q21 S1
G1 E2 F6000
G1 E2 F5000
G1 E2 F5500
G1 E2 F6000
G1 E-15.0000 F5800
G1 E-10.0000 F5500
G1 E-20.0000 F30


; Unload filament
M702 C

G4 ; wait
M221 S100 ; reset flow
M900 K0 ; reset LA

M104 S0 ; turn off temperature
M140 S0 ; turn off heatbed
M107 ; turn off fan
; Lift print head a bit
M73 P21 R1
G1 Z30.15 ; Move print head up
M73 P52 R1
M73 Q52 S1
G1 X0 Y200 F3000 ; home X axis
M84 ; disable motors
M73 P100 R0
M73 Q100 S0
; filament used [mm] = 0.15
; filament used [cm3] = 0.00
; filament used [g] = 0.00
; filament cost = 0.00
; total filament used [g] = 0.00
; total filament cost = 0.00
; estimated printing time (normal mode) = 2m 7s
; estimated printing time (silent mode) = 2m 7s

; prusaslicer_config = begin
; avoid_crossing_perimeters = 0
; avoid_crossing_perimeters_max_detour = 0
; bed_custom_model = 
; bed_custom_texture = 
; bed_shape = 0x0,250x0,250x210,0x210
; bed_temperature = 60,60,60,60,60
; before_layer_gcode = ;BEFORE_LAYER_CHANGE\nG92 E0.0\n;[layer_z]\n\n
; between_objects_gcode = 
; bottom_fill_pattern = rectilinear
; bottom_solid_layers = 8
; bottom_solid_min_thickness = 0.5
; bridge_acceleration = 500
; bridge_angle = 30
; bridge_fan_speed = 100,100,100,100,100
; bridge_flow_ratio = 0.7
; bridge_speed = 30
; brim_separation = 0
; brim_type = outer_only
; brim_width = 0
; clip_multipart_objects = 1
; color_change_gcode = M600
; compatible_printers_condition_cummulative = "printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK3.*/ and nozzle_diameter[0]==0.25";"printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK(2.5|3).*/ and single_extruder_multi_material";"printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK(2.5|3).*/ and single_extruder_multi_material";"printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK(2.5|3).*/ and single_extruder_multi_material";"printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK(2.5|3).*/ and single_extruder_multi_material";"printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK(2.5|3).*/ and single_extruder_multi_material"
; complete_objects = 0
; cooling = 1,1,1,1,1
; cooling_tube_length = 20
; cooling_tube_retraction = 31
; default_acceleration = 1000
; default_filament_profile = "Prusament PLA @MMU2";;;;
; default_print_profile = 0.15mm QUALITY @MK3
; deretract_speed = 0,0,0,0,0
; disable_fan_first_layers = 1,1,1,1,1
; dont_support_bridges = 1
; draft_shield = disabled
; duplicate_distance = 6
; elefant_foot_compensation = 0
; end_filament_gcode = "; Filament-specific end gcode";"; Filament-specific end gcode";"; Filament-specific end gcode";"; Filament-specific end gcode";"; Filament-specific end gcode"
; end_gcode = {if has_wipe_tower}\nG1 E-15.0000 F3000\n{else}\nG1 X0 Y210 F7200\nG1 E2 F5000\nG1 E2 F5500\nG1 E2 F6000\nG1 E2 F5000\nG1 E2 F5500\nG1 E2 F6000\nG1 E-15.0000 F5800\nG1 E-10.0000 F5500\nG1 E-20.0000 F30\n{endif}\n\n; Unload filament\nM702 C\n\nG4 ; wait\nM221 S100 ; reset flow\nM900 K0 ; reset LA\n{if print_settings_id=~/.*(DETAIL @MK3|QUALITY @MK3|SOLUBLE|@0.25 nozzle MK3).*/}M907 E538 ; reset extruder motor current{endif}\nM104 S0 ; turn off temperature\nM140 S0 ; turn off heatbed\nM107 ; turn off fan\n; Lift print head a bit\n{if layer_z < max_print_height}G1 Z{z_offset+min(layer_z+30, max_print_height)}{endif} ; Move print head up\nG1 X0 Y200 F3000 ; home X axis\nM84 ; disable motors\n
; ensure_vertical_shell_thickness = 1
; external_perimeter_extrusion_width = 0.25
; external_perimeter_speed = 20
; external_perimeters_first = 0
; extra_loading_move = -15
; extra_perimeters = 1
; extruder_clearance_height = 20
; extruder_clearance_radius = 45
; extruder_colour = ;;;;
; extruder_offset = 0x0,0x0,0x0,0x0,0x0
; extrusion_axis = E
; extrusion_multiplier = 1,0.95,1,0.95,0.95
; extrusion_width = 0.25
; fan_always_on = 1,1,1,1,1
; fan_below_layer_time = 100,100,100,100,100
; filament_colour = #D2D3D5;#393A41;#F3EEAF;#F0F0F0;#AED5DD
; filament_cooling_final_speed = 2,1,1,1,1
; filament_cooling_initial_speed = 3,2,15,2,2
; filament_cooling_moves = 0,0,2,0,0
; filament_cost = 50,50,50,28.57,35
; filament_density = 1.24,1.24,1.24,1.24,1.24
; filament_diameter = 1.75,1.75,1.75,1.75,1.75
; filament_load_time = 15,21,15,20,20
; filament_loading_speed = 40,25,30,25,25
; filament_loading_speed_start = 15,20,19,20,20
; filament_max_volumetric_speed = 1.5,10,1.5,10,10
; filament_minimal_purge_on_wipe_tower = 1,5,1,5,5
; filament_notes = ;;;;
; filament_ramming_parameters = "130 120| 0.05 2.66451 0.45 3.05805 0.95 4.05807 1.45 5.97742 1.95 7.69999 2.45 8.1936 2.95 11.342 3.45 11.4065 3.95 7.6 4.45 7.6 4.95 7.6";"130 120| 0.05 2.66451 0.45 3.05805 0.95 4.05807 1.45 5.97742 1.95 7.69999 2.45 8.1936 2.95 11.342 3.45 11.4065 3.95 7.6 4.45 7.6 4.95 7.6";"130 120 2.70968 2.87097 3.16129 3.74194 4.80645 6.25806 7.74194 9.03226 10 10.5161| 0.05 2.66451 0.45 2.92902 0.95 4.05807 1.45 6.94516 1.95 9.57096 2.45 10.6452 2.95 11.342 3.45 11.4065 3.95 7.6 4.45 7.6 4.95 7.6";"130 120| 0.05 2.66451 0.45 3.05805 0.95 4.05807 1.45 5.97742 1.95 7.69999 2.45 8.1936 2.95 11.342 3.45 11.4065 3.95 7.6 4.45 7.6 4.95 7.6";"130 120| 0.05 2.66451 0.45 3.05805 0.95 4.05807 1.45 5.97742 1.95 7.69999 2.45 11.0323 2.95 11.342 3.45 11.4065 3.95 7.6 4.45 7.6 4.95 7.6"
; filament_settings_id = "MMU2PLA - Fiberforce_P13-4104TPG-210c-15-40-120-60-mvs1.5";"PLA-MMU2 - Fiberforce_P_19-4104TPG_v5-nRamOrCool";"Test - MatterhackerPro_StuccoBeige-v4";"PLA-MMU2 - Fillamentum-TrafficWhite-v4-nRamOrCool";"MMU2PLA - Fillamentum-CrystlClear-v4-nRamOrCool"
; filament_soluble = 0,0,0,0,0
; filament_spool_weight = 0,0,0,0,0
; filament_toolchange_delay = 0,0,0,0,0
; filament_type = PLA;PLA;PLA;PLA;PLA
; filament_unload_time = 12,30,12,30,30
; filament_unloading_speed = 2,2,30,2,2
; filament_unloading_speed_start = 120,125,125,125,125
; filament_vendor = Prusa Polymers
; fill_angle = 45
; fill_density = 0%
; fill_pattern = line
; first_layer_acceleration = 500
; first_layer_acceleration_over_raft = 0
; first_layer_bed_temperature = 60,60,60,60,60
; first_layer_extrusion_width = 0.25
; first_layer_height = 0.15
; first_layer_speed = 30
; first_layer_speed_over_raft = 30
; first_layer_temperature = 210,210,220,205,220
; full_fan_speed_layer = 0,0,0,0,0
; fuzzy_skin = none
; fuzzy_skin_point_dist = 0.8
; fuzzy_skin_thickness = 0.3
; gap_fill_enabled = 1
; gap_fill_speed = 30
; gcode_comments = 0
; gcode_flavor = marlin
; gcode_label_objects = 0
; gcode_resolution = 0.0125
; high_current_on_filament_swap = 0
; host_type = octoprint
; infill_acceleration = 1000
; infill_anchor = 600%
; infill_anchor_max = 50
; infill_every_layers = 1
; infill_extruder = 1
; infill_extrusion_width = 0.5
; infill_first = 0
; infill_only_where_needed = 0
; infill_overlap = 25%
; infill_speed = 35
; inherits_cummulative = ;;;;;;"Original Prusa i3 MK3S MMU2S"
; interface_shells = 0
; ironing = 0
; ironing_flowrate = 15%
; ironing_spacing = 0.1
; ironing_speed = 15
; ironing_type = top
; layer_gcode = ;AFTER_LAYER_CHANGE\n;[layer_z]
; layer_height = 0.07
; machine_limits_usage = emit_to_gcode
; machine_max_acceleration_e = 4000,4000
; machine_max_acceleration_extruding = 800,500
; machine_max_acceleration_retracting = 800,500
; machine_max_acceleration_travel = 1500,1250
; machine_max_acceleration_x = 800,500
; machine_max_acceleration_y = 800,500
; machine_max_acceleration_z = 200,200
; machine_max_feedrate_e = 120,120
; machine_max_feedrate_x = 200,100
; machine_max_feedrate_y = 200,100
; machine_max_feedrate_z = 12,12
; machine_max_jerk_e = 4.5,4.5
; machine_max_jerk_x = 6,6
; machine_max_jerk_y = 6,6
; machine_max_jerk_z = 0.4,0.4
; machine_min_extruding_rate = 0,0
; machine_min_travel_rate = 0,0
; max_fan_speed = 100,100,100,100,100
; max_layer_height = 0.15,0.15,0.15,0.15,0.15
; max_print_height = 210
; max_print_speed = 50
; max_volumetric_speed = 0
; min_fan_speed = 100,100,100,100,100
; min_layer_height = 0.05,0.05,0.05,0.05,0.05
; min_print_speed = 15,15,15,15,15
; min_skirt_length = 4
; mmu_segmented_region_max_width = 0
; notes = 
; nozzle_diameter = 0.25,0.25,0.25,0.25,0.25
; only_retract_when_crossing_perimeters = 0
; ooze_prevention = 0
; output_filename_format = {input_filename_base}_{nozzle_diameter[0]}x{layer_height}_{print_time}.gcode
; overhangs = 1
; parking_pos_retraction = 72
; pause_print_gcode = M601
; perimeter_acceleration = 500
; perimeter_extruder = 1
; perimeter_extrusion_width = 0.25
; perimeter_speed = 35
; perimeters = 5
; physical_printer_settings_id = 
; post_process = 
; print_settings_id = CRC_Shapiros_25x07x24mms
; printer_model = MK3SMMU2S
; printer_notes = Don't remove the following keywords! These keywords are used in the "compatible printer" condition of the print and filament profiles to link the particular print and filament profiles to this printer profile.\nPRINTER_VENDOR_PRUSA3D\nPRINTER_MODEL_MK3\n
; printer_settings_id = v10_SkMnsMMU2S_n025
; printer_technology = FFF
; printer_variant = 0.4
; printer_vendor = 
; raft_contact_distance = 0.1
; raft_expansion = 1.5
; raft_first_layer_density = 90%
; raft_first_layer_expansion = 3
; raft_layers = 0
; remaining_times = 1
; resolution = 0
; retract_before_travel = 1,1,1,1,1
; retract_before_wipe = 0%,0%,0%,0%,0%
; retract_layer_change = 1,1,1,1,1
; retract_length = 0.6,0.8,0.8,0.8,0.8
; retract_length_toolchange = 3,3,3,3,3
; retract_lift = 0,0.25,0.25,0.25,0.25
; retract_lift_above = 0.18,0,0,0,0
; retract_lift_below = 209,209,209,209,209
; retract_restart_extra = 0,0,0,0,0
; retract_restart_extra_toolchange = 0,0,0,0,0
; retract_speed = 30,35,35,35,35
; seam_position = nearest
; silent_mode = 1
; single_extruder_multi_material = 1
; single_extruder_multi_material_priming = 0
; skirt_distance = 2
; skirt_height = 3
; skirts = 0
; slice_closing_radius = 0.049
; slicing_mode = regular
; slowdown_below_layer_time = 20,20,20,20,20
; small_perimeter_speed = 16
; solid_infill_below_area = 1
; solid_infill_every_layers = 0
; solid_infill_extruder = 1
; solid_infill_extrusion_width = 0.25
; solid_infill_speed = 30
; spiral_vase = 0
; standby_temperature_delta = -5
; start_filament_gcode = "M900 K0";"M900 K{if printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.6}0.12{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/}0.2{elsif nozzle_diameter[0]==0.6}0.04{else}0.05{endif} ; Filament gcode LA 1.5\n{if printer_notes=~/.*PRINTER_MODEL_MINI.*/};{elsif printer_notes=~/.*PRINTER_HAS_BOWDEN.*/}M900 K200{elsif nozzle_diameter[0]==0.6}M900 K18{else}M900 K30{endif} ; Filament gcode LA 1.0";"M900 K{if printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.6}0.12{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/}0.2{elsif nozzle_diameter[0]==0.6}0.04{else}0.05{endif} ; Filament gcode LA 1.5\n{if printer_notes=~/.*PRINTER_MODEL_MINI.*/};{elsif printer_notes=~/.*PRINTER_HAS_BOWDEN.*/}M900 K200{elsif nozzle_diameter[0]==0.6}M900 K18{else}M900 K30{endif} ; Filament gcode LA 1.0";"M900 K{if printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.6}0.12{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/}0.2{elsif nozzle_diameter[0]==0.6}0.04{else}0.05{endif} ; Filament gcode LA 1.5\n{if printer_notes=~/.*PRINTER_MODEL_MINI.*/};{elsif printer_notes=~/.*PRINTER_HAS_BOWDEN.*/}M900 K200{elsif nozzle_diameter[0]==0.6}M900 K18{else}M900 K30{endif} ; Filament gcode LA 1.0";"M900 K{if printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.6}0.12{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/}0.2{elsif nozzle_diameter[0]==0.6}0.04{else}0.05{endif} ; Filament gcode LA 1.5\n{if printer_notes=~/.*PRINTER_MODEL_MINI.*/};{elsif printer_notes=~/.*PRINTER_HAS_BOWDEN.*/}M900 K200{elsif nozzle_diameter[0]==0.6}M900 K18{else}M900 K30{endif} ; Filament gcode LA 1.0"
; start_gcode = M862.3 P "[printer_model]" ; printer model check\nM862.1 P[nozzle_diameter] ; nozzle diameter check\nM115 U3.9.1 ; tell printer latest fw version\nG90 ; use absolute coordinates\nM83 ; extruder relative mode\nM104 S[first_layer_temperature] ; set extruder temp\nM140 S[first_layer_bed_temperature] ; set bed temp\nM190 S[first_layer_bed_temperature] ; wait for bed temp\nM109 S[first_layer_temperature] ; wait for extruder temp\nG28 W ; home all without mesh bed level\nG80 ; mesh bed leveling\n\n;Skelestruder Code Start - Currently managed by custom Firmware\n;M350 E16 ; 16 Microsteps instead of 32\n;M92 E492 ; 492 steps/mm instead of 280  Flow Test result was 492\n;M221 S95 ; Set flow to tested Stable 95%\n;Skelestruder Code End\n\n; Send the filament type to the MMU2.0 unit.\n; E stands for extruder number, F stands for filament type (0: default; 1:flex; 2: PVA)\nM403 E0 F{"" + ((filament_type[0]=="FLEX") ? 1 : ((filament_type[0]=="PVA") ? 2 : 0))}\nM403 E1 F{"" + ((filament_type[1]=="FLEX") ? 1 : ((filament_type[1]=="PVA") ? 2 : 0))}\nM403 E2 F{"" + ((filament_type[2]=="FLEX") ? 1 : ((filament_type[2]=="PVA") ? 2 : 0))}\nM403 E3 F{"" + ((filament_type[3]=="FLEX") ? 1 : ((filament_type[3]=="PVA") ? 2 : 0))}\nM403 E4 F{"" + ((filament_type[4]=="FLEX") ? 1 : ((filament_type[4]=="PVA") ? 2 : 0))}\n\n{if not has_single_extruder_multi_material_priming}\n;go outside print area\nG1 Y-3.0 F1000.0\nG1 Z0.4 F1000.0\n; select extruder\nT[initial_tool]\n; initial load\nG1 X55.0 E29.0 F1073.0\nG1 X5.0 E15.0 F1800.0\nG1 X55.0 E8.0 F2000.0\nG1 Z0.3 F1000.0\nG92 E0.0\nG1 X240.0 E25.0 F2200.0\nG1 Y-2.0 F1000.0\nG1 X55.0 E25 F1400.0\nG1 Z0.20 F1000.0\nG1 X5.0 E4.0 F1000.0\nG92 E0.0\n{endif}\n\n;M221 S{if layer_height<0.075}100{else}95{endif}\nG92 E0.0\n\n; Don't change E values below. Excessive value can damage the printer.\n{if print_settings_id=~/.*(DETAIL @MK3|QUALITY @MK3|SOLUBLE).*/}M907 E430 ; set extruder motor current{endif}\n{if print_settings_id=~/.*(SPEED @MK3|DRAFT @MK3).*/}M907 E538 ; set extruder motor current{endif}
; support_material = 0
; support_material_angle = 90
; support_material_auto = 0
; support_material_bottom_contact_distance = 0
; support_material_bottom_interface_layers = -1
; support_material_buildplate_only = 0
; support_material_closing_radius = 2
; support_material_contact_distance = 0
; support_material_enforce_layers = 0
; support_material_extruder = 2
; support_material_extrusion_width = 0.2
; support_material_interface_contact_loops = 0
; support_material_interface_extruder = 1
; support_material_interface_layers = 2
; support_material_interface_pattern = rectilinear
; support_material_interface_spacing = 0.25
; support_material_interface_speed = 100%
; support_material_pattern = rectilinear
; support_material_spacing = 0.5
; support_material_speed = 30
; support_material_style = grid
; support_material_synchronize_layers = 1
; support_material_threshold = 55
; support_material_with_sheath = 0
; support_material_xy_spacing = 150%
; temperature = 210,205,225,215,230
; template_custom_gcode = 
; thick_bridges = 1
; thin_walls = 0
; threads = 12
; thumbnails = 
; toolchange_gcode = 
; top_fill_pattern = monotonic
; top_infill_extrusion_width = 0.25
; top_solid_infill_speed = 20
; top_solid_layers = 9
; top_solid_min_thickness = 0.5
; travel_speed = 180
; travel_speed_z = 0
; use_firmware_retraction = 0
; use_relative_e_distances = 1
; use_volumetric_e = 0
; variable_layer_height = 1
; wipe = 0,1,1,1,1
; wipe_into_infill = 0
; wipe_into_objects = 0
; wipe_tower = 1
; wipe_tower_bridging = 6
; wipe_tower_brim_width = 2
; wipe_tower_no_sparse_layers = 1
; wipe_tower_rotation_angle = 0
; wipe_tower_width = 100
; wipe_tower_x = 72.6871
; wipe_tower_y = 162.82
; wiping_volumes_extruders = 70,70,70,70,70,70,70,70,70,70
; wiping_volumes_matrix = 0,140,140,140,140,140,0,140,140,140,140,140,0,140,140,140,140,140,0,140,140,140,140,140,0
; xy_size_compensation = 0
; z_offset = 0
; prusaslicer_config = end
