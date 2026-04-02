// QR Code Stand for Business Cards
// Designed for Orderforge
// Print settings: 0.2mm layer height, 15% infill, supports recommended for overhang

// Dimensions
base_width = 85;      // Standard business card width
base_depth = 60;      // Standard business card height
base_height = 8;
stand_angle = 70;      // Viewing angle

// Card slot dimensions
card_slot_width = 87;
card_slot_depth = 3;
card_slot_offset = 5;

// QR display area
qr_display_width = 40;
qr_display_height = 40;
qr_stand_thickness = 3;

// Base module
module base() {
    difference() {
        cube([base_width, base_depth, base_height]);
        // Card slot
        translate([(base_width - card_slot_width)/2, -1, base_height - card_slot_depth])
            cube([card_slot_width, base_depth + 2, card_slot_depth + 1]);
    }
}

// QR code display stand
module qr_stand() {
    rotate([stand_angle, 0, 0])
    difference() {
        cube([qr_display_width, qr_stand_thickness, qr_display_height]);
        // Recessed area for QR code sticker/display
        translate([2, -1, 2])
            cube([qr_display_width - 4, qr_stand_thickness + 2, qr_display_height - 4]);
    }
}

// Full assembly
module qr_card_stand() {
    // Base with card slot
    base();
    
    // QR display on back
    translate([(base_width - qr_display_width)/2, base_depth - 10, base_height])
        qr_stand();
    
    // Support for QR stand
    translate([(base_width - qr_display_width)/2, base_depth - 10, base_height])
        cube([qr_display_width, 8, 2]);
}

// Render
qr_card_stand();

// Alternative: Simpler angled stand
module simple_card_stand() {
    union() {
        // Angled back
        rotate([-stand_angle, 0, 0])
            cube([base_width, qr_stand_thickness, base_depth]);
        
        // Base
        cube([base_width, 15, 8]);
        
        // Lip at bottom
        translate([0, 0, 0])
            cube([base_width, 3, 10]);
    }
}

// Uncomment for simpler version:
// translate([100, 0, 0]) simple_card_stand();
