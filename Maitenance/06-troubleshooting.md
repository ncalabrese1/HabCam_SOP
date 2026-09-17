# Troubleshooting

## Fiber Optics

Inside the HabCam main electronics bottle there are four media converters: one for each camera, one for the data network (all other sensors, sonars, moxas, gardasofts, expansion bottle, and the chanos sensor), and a spare port not actively used. When the vehicle is powered on, full link lights on the front of each media converter indicate functional fiber optic connectivity per channel.

Multiple junctions (coupling points) exist throughout the system where improper seating or contamination will cause data loss.

---

### Connection Flowchart

```{mermaid}
graph TD
    subgraph Submerged["Submerged Connections"]
        direction TD
        
        subgraph Sub_Inputs[" "]
            direction LR
            Cam1_Sub["Cam1"]
            Cam2_Sub["Cam2"]
            Data_Sub["Data Network"]
            Spare_Sub["Spare"]
        end

        Mux_Sub(["Multiplexer"])

        Cam1_Sub --> Mux_Sub
        Cam1_Sub --> Mux_Sub
        Cam2_Sub --> Mux_Sub
        Cam2_Sub --> Mux_Sub
        Data_Sub --> Mux_Sub
        Data_Sub --> Mux_Sub
        Spare_Sub --> Mux_Sub
        Spare_Sub --> Mux_Sub

        Mux_Sub --> Bulkhead{"Fiber Optic<br/>Bulkhead"}
        Bulkhead -->|⬇️<br/>Common Issue| FOCable{"Fiber Optic<br/>Cable"}
        FOCable --> OFJBox(["Oil Filled<br/>Junction Box"])
    end

    OFJBox --> WinchCable(("Winch Cable"))

    subgraph TopSide["Top-side Connections"]
        direction TD
        WinchCable --> SlipRing(["Winch<br/>Slip Ring"])
        SlipRing -->|⬇️<br/>Common Issue| DryLabJBox(["Dry Lab<br/>Junction Box"])
        DryLabJBox -->|⬇️<br/>Common Issue| Mux_Top(["Multiplexer"])
        
        Mux_Top --> Cam1_Top
        Mux_Top --> Cam1_Top
        Mux_Top --> Cam2_Top
        Mux_Top --> Cam2_Top
        Mux_Top --> Data_Top
        Mux_Top --> Data_Top
        Mux_Top --> Spare_Top
        Mux_Top --> Spare_Top

        subgraph Top_Outputs[" "]
            direction LR
            Cam1_Top["Cam1"]
            Cam2_Top["Cam2"]
            Data_Top["Data Network"]
            Spare_Top["Spare"]
        end
    end

    %% Diagram Styling
    style Submerged fill:#ffffff,stroke:#4a90e2,stroke-width:1.5px,stroke-dasharray: 4 4
    style TopSide fill:#ffffff,stroke:#f5a623,stroke-width:1.5px,stroke-dasharray: 4 4
    style Sub_Inputs fill:none,stroke:none
    style Top_Outputs fill:none,stroke:none
    style Mux_Sub fill:#ffffff,stroke:#000000,stroke-width:2px
    style Mux_Top fill:#ffffff,stroke:#000000,stroke-width:2px
    style OFJBox fill:#ffffff,stroke:#000000,stroke-width:2px
    style SlipRing fill:#ffffff,stroke:#000000,stroke-width:2px
    style DryLabJBox fill:#ffffff,stroke:#000000,stroke-width:2px
    style WinchCable fill:#ffffff,stroke:#000000,stroke-width:2px
```

---

---

::: {.grid}

::: {.g-col-12 .g-col-md-6}
::: {.callout-warning appearance="simple"}
### Inspection Checklist
Carefully inspect designated high-failure points:

* **OptoLink bulkhead & mating cable** on the main electronics bottle
* **Ship's slip ring** assembly
* **Dry lab junction box to demultiplexer** interconnects
:::
:::

::: {.g-col-12 .g-col-md-6}
::: {.callout-note appearance="simple"}
### Cleaning Protocols
* **ST Connectors:** Clean using isopropyl alcohol and CLETOP fiber optic wipes. Use fiber optic insert cleaning pens for couplers.
* **Subconn OptoLink Series:** Ensure mating surfaces are dry and clean using **only** isopropyl alcohol and Kimtech wipes. Apply **Molykote Series 55** o-ring grease to o-rings.
:::
:::

:::
