import gradio as gr
from matplotlib.figure import Figure

from magma_viscosity_calculator import (
    MAGMA_TYPES,
    TEMP_MIN_C,
    TEMP_MAX_C,
    WATER_MIN_WT,
    WATER_MAX_WT,
    calculate_viscosity,
    compute_viscosity_curve,
)


def _build_plot(temperatures, log_values, selected_temperature):
    fig = Figure(figsize=(6.0, 4.0), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot(
        temperatures,
        log_values,
        color="#1f77b4",
        linewidth=2.0,
        marker="o",
        markersize=2.0,
        label="log10 η (Pa·s)",
    )
    ax.axvline(
        selected_temperature,
        color="red",
        linestyle="--",
        linewidth=1.5,
        label=f"Selected T = {selected_temperature:.0f} °C",
    )

    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("log10 viscosity (Pa·s)")
    ax.set_title("Magma viscosity vs temperature (VFT)")
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.legend(loc="best")

    fig.tight_layout()
    return fig


def calculate(magma_type, temperature_c, water_wt):
    if magma_type is None or temperature_c is None or water_wt is None:
        return "Please provide magma composition, temperature, and water content.", None

    try:
        log_eta, eta = calculate_viscosity(magma_type, temperature_c, water_wt)
        temperatures, log_values, _ = compute_viscosity_curve(
            magma_type,
            temperature_c,
            water_wt,
        )
        fig = _build_plot(temperatures, log_values, float(temperature_c))

        result = (
            "**Magma viscosity estimate**\n\n"
            f"- Composition: {magma_type}\n"
            f"- Temperature: {float(temperature_c):.1f} °C\n"
            f"- Water content: {float(water_wt):.1f} wt%\n"
            f"- log10(η): {log_eta:.3f}\n"
            f"- η: {eta:.3e} Pa·s"
        )
        return result, fig

    except Exception as exc:
        return f"Invalid input: {exc}", None


demo = gr.Interface(
    fn=calculate,
    inputs=[
        gr.Dropdown(
            choices=MAGMA_TYPES,
            value="Basalt",
            label="Magma composition",
        ),
        gr.Number(
            value=1000.0,
            minimum=TEMP_MIN_C,
            maximum=TEMP_MAX_C,
            step=1,
            precision=0,
            label="Temperature (°C)",
        ),
        gr.Number(
            value=0.0,
            minimum=WATER_MIN_WT,
            maximum=WATER_MAX_WT,
            step=0.1,
            precision=1,
            label="Water content (wt%)",
        ),
    ],
    outputs=[
        gr.Markdown(label="Result"),
        gr.Plot(label="Viscosity curve"),
    ],
    title="Magma Viscosity Calculator",
    description="Estimates magma viscosity in Pa·s using the VFT equation with a water-content correction.",
)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
