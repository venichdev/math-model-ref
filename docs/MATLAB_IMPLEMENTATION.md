# MATLAB Implementation Guide

## Clean, Token-Efficient MATLAB Code

This guide provides MATLAB implementations without emojis or special characters.
All code is optimized for:
- Clean variable names
- Minimal token usage
- MATLAB compatibility
- Easy copy-paste

---

## Basic EV Range Calculator

### 1. Vehicle Parameters

```matlab
% Vehicle parameters (simple variable names)
m = 1800;           % Vehicle mass [kg]
A = 2.3;            % Frontal area [m^2]
Cd = 0.28;          % Drag coefficient [-]
Cr = 0.010;         % Rolling resistance coefficient [-]
rho = 1.2;          % Air density [kg/m^3]
g = 9.81;           % Gravity [m/s^2]

% Battery parameters
Q_batt = 75;        % Battery capacity [kWh]
Q_use = 70;         % Usable capacity [kWh]
V_nom = 400;        % Nominal voltage [V]
SOC_init = 1.0;     % Initial SOC [-]

% Powertrain parameters
eta_motor = 0.95;   % Motor efficiency [-]
eta_trans = 0.97;   % Transmission efficiency [-]
eta_inv = 0.96;     % Inverter efficiency [-]
eta_total = eta_motor * eta_trans * eta_inv;

% Auxiliary loads
P_aux = 2.0;        % Auxiliary power [kW]
```

### 2. Force Calculations

```matlab
% Aerodynamic drag force
function F_aero = calc_aero_drag(v, Cd, A, rho)
    F_aero = 0.5 * rho * Cd * A * v^2;
end

% Rolling resistance force
function F_roll = calc_rolling_resistance(m, Cr, g)
    F_roll = m * g * Cr;
end

% Grading resistance force
function F_grade = calc_grade_resistance(m, g, grade)
    theta = atan(grade);
    F_grade = m * g * sin(theta);
end

% Total tractive force
function F_total = calc_total_force(m, a, v, Cd, A, rho, Cr, g, grade)
    F_accel = m * a;
    F_aero = calc_aero_drag(v, Cd, A, rho);
    F_roll = calc_rolling_resistance(m, Cr, g);
    F_grade = calc_grade_resistance(m, g, grade);
    F_total = F_accel + F_aero + F_roll + F_grade;
end
```

### 3. Energy Consumption Calculation

```matlab
% Highway range calculation
function results = calc_highway_range(speed_kmh, duration_s, params)
    % Convert speed
    v = speed_kmh / 3.6;  % [m/s]

    % Time vector
    t = 0:1:duration_s;
    N = length(t);

    % Calculate forces (constant speed, a=0)
    F_aero = calc_aero_drag(v, params.Cd, params.A, params.rho);
    F_roll = calc_rolling_resistance(params.m, params.Cr, params.g);
    F_total = F_aero + F_roll;

    % Power at wheels
    P_wheels = F_total * v / 1000;  % [kW]

    % Power from battery
    P_motor = P_wheels / params.eta_total;
    P_battery = P_motor + params.P_aux;

    % Energy consumption
    E_total = P_battery * duration_s / 3600;  % [kWh]

    % Distance
    dist = v * duration_s / 1000;  % [km]

    % Consumption rate
    cons_per_100km = E_total / dist * 100;  % [kWh/100km]

    % Range estimation
    range_km = params.Q_use / (E_total / dist);

    % SOC final
    SOC_final = params.SOC_init - E_total / params.Q_batt;

    % Pack results
    results.distance_km = dist;
    results.energy_kWh = E_total;
    results.consumption_per_100km = cons_per_100km;
    results.range_km = range_km;
    results.SOC_final = SOC_final;
    results.P_wheels = P_wheels;
    results.P_battery = P_battery;
end
```

### 4. Battery SOC Tracking

```matlab
% Coulomb counting SOC estimation
function SOC_new = update_SOC(SOC_prev, current, dt, Q_Ah, eta)
    % SOC(t+dt) = SOC(t) - (eta * I * dt) / (3600 * Q)
    dSOC = -(eta * current * dt) / (3600 * Q_Ah);
    SOC_new = SOC_prev + dSOC;
    SOC_new = max(0.0, min(1.0, SOC_new));  % Clamp [0,1]
end

% Battery capacity in Ah
function Q_Ah = get_capacity_Ah(Q_kWh, V_nom)
    Q_Ah = (Q_kWh * 1000) / V_nom;
end
```

### 5. Drive Cycle Simulation

```matlab
% WLTP-like cycle simulation
function results = simulate_drive_cycle(t, v, params)
    N = length(t);

    % Preallocate arrays
    F_total = zeros(N, 1);
    P_wheels = zeros(N, 1);
    P_battery = zeros(N, 1);
    SOC = zeros(N, 1);
    SOC(1) = params.SOC_init;

    % Calculate acceleration
    a = gradient(v) ./ gradient(t);

    % Loop through time steps
    for i = 1:N
        % Calculate forces
        F_total(i) = calc_total_force(params.m, a(i), v(i), ...
            params.Cd, params.A, params.rho, params.Cr, params.g, 0);

        % Power at wheels
        P_wheels(i) = F_total(i) * v(i) / 1000;  % [kW]

        % Power from battery (simplified, no regen)
        if P_wheels(i) > 0
            P_battery(i) = P_wheels(i) / params.eta_total + params.P_aux;
        else
            P_battery(i) = params.P_aux;
        end

        % Update SOC
        if i > 1
            dt = t(i) - t(i-1);
            I = P_battery(i) * 1000 / params.V_nom;  % [A]
            Q_Ah = get_capacity_Ah(params.Q_batt, params.V_nom);
            SOC(i) = update_SOC(SOC(i-1), I, dt, Q_Ah, 0.99);
        end
    end

    % Calculate total energy
    E_total = trapz(t, P_battery) / 3600;  % [kWh]
    dist = trapz(t, v) / 1000;  % [km]
    cons_per_100km = E_total / dist * 100;
    range_km = params.Q_use / (E_total / dist);

    % Pack results
    results.time = t;
    results.velocity = v;
    results.SOC = SOC;
    results.P_wheels = P_wheels;
    results.P_battery = P_battery;
    results.distance_km = dist;
    results.energy_kWh = E_total;
    results.consumption_per_100km = cons_per_100km;
    results.range_km = range_km;
    results.SOC_final = SOC(end);
end
```

### 6. Temperature Impact on Range

```matlab
% Range adjustment for temperature
function range_adj = adjust_range_temperature(range_base, T_ambient)
    T_opt = 21.5;           % Optimal temperature [C]
    k_temp = 0.0001;        % Temperature coefficient [1/C^2]

    % Temperature factor
    f_temp = 1 - k_temp * (T_ambient - T_opt)^2;
    f_temp = max(0.5, f_temp);  % Minimum 50%

    % HVAC factor
    if abs(T_ambient - 22) > 10
        f_hvac = 0.80;
    elseif abs(T_ambient - 22) > 5
        f_hvac = 0.90;
    else
        f_hvac = 0.98;
    end

    % Adjusted range
    range_adj = range_base * f_temp * f_hvac;
end
```

---

## Complete Example Script

```matlab
% EV Range Calculator - Clean MATLAB Implementation
% No emojis, simple variables, token-efficient

clear; clc;

% Define parameters structure
params.m = 1800;
params.A = 2.3;
params.Cd = 0.28;
params.Cr = 0.010;
params.rho = 1.2;
params.g = 9.81;
params.Q_batt = 75;
params.Q_use = 70;
params.V_nom = 400;
params.SOC_init = 1.0;
params.eta_motor = 0.95;
params.eta_trans = 0.97;
params.eta_inv = 0.96;
params.eta_total = params.eta_motor * params.eta_trans * params.eta_inv;
params.P_aux = 2.0;

% Highway range test at 120 km/h for 1 hour
fprintf('Highway Range Test (120 km/h, 1 hour)\n');
fprintf('=====================================\n');

results = calc_highway_range(120, 3600, params);

fprintf('Distance:     %.1f km\n', results.distance_km);
fprintf('Energy:       %.2f kWh\n', results.energy_kWh);
fprintf('Consumption:  %.2f kWh/100km\n', results.consumption_per_100km);
fprintf('Range:        %.0f km\n', results.range_km);
fprintf('SOC:          %.0f%% -> %.1f%%\n', ...
    params.SOC_init*100, results.SOC_final*100);
fprintf('Power wheels: %.2f kW\n', results.P_wheels);
fprintf('Power batt:   %.2f kW\n\n', results.P_battery);

% Temperature impact analysis
fprintf('Temperature Impact Analysis\n');
fprintf('===========================\n');
T_range = -20:5:40;
range_base = results.range_km;

for i = 1:length(T_range)
    T = T_range(i);
    range_T = adjust_range_temperature(range_base, T);
    loss = (1 - range_T/range_base) * 100;
    fprintf('T = %3d C:  Range = %3.0f km  (Loss: %4.1f%%)\n', ...
        T, range_T, loss);
end
```

---

## Plotting Results (Clean Style)

```matlab
% Clean plotting without special characters
function plot_drive_cycle(results)
    figure('Position', [100 100 1000 800]);

    % Convert to minutes
    t_min = results.time / 60;
    v_kmh = results.velocity * 3.6;

    % Plot 1: Velocity
    subplot(3,1,1);
    plot(t_min, v_kmh, 'b-', 'LineWidth', 1.5);
    ylabel('Speed [km/h]');
    title('Drive Cycle Simulation Results');
    grid on;

    % Plot 2: Power
    subplot(3,1,2);
    plot(t_min, results.P_wheels, 'g-', 'LineWidth', 1.5); hold on;
    plot(t_min, results.P_battery, 'r-', 'LineWidth', 1.5);
    plot([t_min(1) t_min(end)], [0 0], 'k--', 'LineWidth', 0.8);
    ylabel('Power [kW]');
    legend('Wheel Power', 'Battery Power', 'Location', 'best');
    grid on;

    % Plot 3: SOC
    subplot(3,1,3);
    plot(t_min, results.SOC*100, 'Color', [0.5 0 0.5], 'LineWidth', 2);
    ylabel('SOC [%]');
    xlabel('Time [minutes]');
    ylim([0 105]);
    grid on;

    % Add text summary
    annotation('textbox', [0.15 0.02 0.7 0.05], ...
        'String', sprintf(['Distance: %.1f km | Energy: %.2f kWh | ' ...
        'Consumption: %.2f kWh/100km | Range: %.0f km'], ...
        results.distance_km, results.energy_kWh, ...
        results.consumption_per_100km, results.range_km), ...
        'EdgeColor', 'none', 'FontSize', 10);
end
```

---

## Simple Drive Cycle Generation

```matlab
% Constant speed cycle
function [t, v] = generate_constant_speed(speed_kmh, duration_s, dt)
    t = 0:dt:duration_s;
    v = ones(size(t)) * (speed_kmh / 3.6);  % Convert to m/s
end

% Urban cycle (stop-and-go)
function [t, v] = generate_urban_cycle(duration_s, dt)
    t = 0:dt:duration_s;
    N = length(t);
    v = zeros(N, 1);

    seg_dur = 100;  % Segment duration [s]

    for i = 1:N
        t_seg = mod(t(i), seg_dur);

        if t_seg < 20
            v(i) = (t_seg / 20) * 50;       % Accelerate to 50 km/h
        elseif t_seg < 60
            v(i) = 50;                       % Cruise
        elseif t_seg < 80
            v(i) = 50 - ((t_seg - 60) / 20) * 50;  % Decelerate
        else
            v(i) = 0;                        % Stop
        end
    end

    v = v / 3.6;  % Convert to m/s
end

% WLTP-like cycle (simplified)
function [t, v] = generate_wltp_cycle(duration_s, dt)
    t = 0:dt:duration_s;
    N = length(t);
    v = zeros(N, 1);

    for i = 1:N
        phase = mod(t(i), 600) / 600;

        if phase < 0.25
            v(i) = 20 + 15 * sin(2*pi*phase*4);
        elseif phase < 0.5
            v(i) = 40 + 20 * sin(2*pi*(phase-0.25)*4);
        elseif phase < 0.75
            v(i) = 60 + 15 * sin(2*pi*(phase-0.5)*4);
        else
            v(i) = 80 + 20 * sin(2*pi*(phase-0.75)*4);
        end
    end

    v = v / 3.6;  % Convert to m/s
end
```

---

## Variable Naming Convention

Use simple, clear names without special characters:

| Good (MATLAB-safe) | Avoid |
|--------------------|-------|
| `m` | `m_vehicle` with special chars |
| `Cd` | `C_d` or `Cₐ` |
| `eta_motor` | `η_motor` |
| `rho` | `ρ` |
| `theta` | `θ` |
| `SOC` | `SOC%` or emojis |
| `P_aux` | `P_aux_💡` |
| `F_total` | `F_total⃗` |
| `Q_batt` | `Q_batt🔋` |
| `v_kmh` | `v_km/h` |

---

## Token-Efficient Code Style

Minimize tokens while maintaining clarity:

```matlab
% Good: Short, clear, efficient
m = 1800; A = 2.3; Cd = 0.28;
F = 0.5 * rho * Cd * A * v^2;

% Avoid: Long names waste tokens
vehicle_mass_in_kilograms = 1800;
frontal_area_in_square_meters = 2.3;
aerodynamic_drag_coefficient = 0.28;
aerodynamic_force = 0.5 * air_density * ...
    aerodynamic_drag_coefficient * ...
    frontal_area_in_square_meters * velocity_squared;
```

---

## Complete Validation Script

```matlab
% Nissan Leaf 2018 Validation (Clean Code)
clear; clc;

% Nissan Leaf parameters
p.m = 1580;
p.A = 2.27;
p.Cd = 0.28;
p.Cr = 0.009;
p.rho = 1.2;
p.g = 9.81;
p.Q_batt = 40;
p.Q_use = 38;
p.V_nom = 350;
p.SOC_init = 1.0;
p.eta_motor = 0.92;
p.eta_trans = 0.96;
p.eta_inv = 0.96;
p.eta_total = p.eta_motor * p.eta_trans * p.eta_inv;
p.P_aux = 0.3;

% City cycle
[t_city, v_city] = generate_urban_cycle(1400, 1);
res_city = simulate_drive_cycle(t_city, v_city, p);

% Highway cycle
[t_hwy, v_hwy] = generate_constant_speed(100, 1800, 1);
res_hwy = simulate_drive_cycle(t_hwy, v_hwy, p);

% EPA data
epa_city = 18.9;
epa_hwy = 20.8;
epa_range = 203;

% Model results
mod_city = res_city.consumption_per_100km;
mod_hwy = res_hwy.consumption_per_100km;
mod_range = p.Q_use / res_city.energy_kWh * res_city.distance_km;

% Errors
err_city = (mod_city - epa_city) / epa_city * 100;
err_hwy = (mod_hwy - epa_hwy) / epa_hwy * 100;
err_range = (mod_range - epa_range) / epa_range * 100;

% Display
fprintf('Nissan Leaf 2018 Validation\n');
fprintf('===========================\n');
fprintf('Metric          EPA      Model    Error\n');
fprintf('City [kWh/100]  %.1f     %.1f    %+.1f%%\n', ...
    epa_city, mod_city, err_city);
fprintf('Hwy [kWh/100]   %.1f     %.1f    %+.1f%%\n', ...
    epa_hwy, mod_hwy, err_hwy);
fprintf('Range [km]      %.0f      %.0f     %+.1f%%\n', ...
    epa_range, mod_range, err_range);
```

---

## Summary

Key principles for clean MATLAB code:
- Simple variable names (m, Cd, eta, SOC)
- No emojis or special Unicode
- Short, clear comments
- Token-efficient naming
- Standard MATLAB syntax
- Easy copy-paste compatibility

All mathematical accuracy maintained while using minimal tokens.
