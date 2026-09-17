# Troubleshooting

## Fiber Optics

Inside the HabCam main electronics bottle there are four media converters: one for each camera, one for the data network (all other sensors, sonars, moxas, gardasofts, expansion bottle, and the chanos sensor), and a spare port not actively used. When the vehicle is powered on, full link lights on the front of each media converter indicate functional fiber optic connectivity per channel.

Multiple junctions (coupling points) exist throughout the system where improper seating or contamination will cause data loss.

---

### Connection Flowchart

```{=html}
<div class="d-flex flex-column align-items-center my-4">

  <!-- Submerged Connections Container -->
  <div class="border border-primary rounded p-4 w-100 position-relative bg-light text-center" style="max-width: 650px; border-style: dashed !important;">
    <span class="badge bg-primary position-absolute top-0 start-0 translate-middle-y ms-3 fs-6">Submerged Connections</span>
    
    <div class="row g-2 justify-content-center mb-3 mt-2">
      <div class="col-auto"><span class="badge bg-secondary p-2">Cam1</span></div>
      <div class="col-auto"><span class="badge bg-secondary p-2">Cam2</span></div>
      <div class="col-auto"><span class="badge bg-secondary p-2">Data Network</span></div>
      <div class="col-auto"><span class="badge bg-secondary p-2">Spare</span></div>
    </div>
    
    <div class="text-secondary fs-4">&#8595;</div>
    
    <div class="card mx-auto my-2 shadow-sm" style="max-width: 320px;">
      <div class="card-body p-2 fw-bold bg-white">Submerged Multiplexer</div>
    </div>
    
    <div class="text-secondary fs-4">&#8595;</div>
    
    <div class="card mx-auto my-2 shadow-sm" style="max-width: 320px;">
      <div class="card-body p-2 bg-white">Fiber Optic Bulkhead</div>
    </div>
    
    <div class="text-secondary fs-4">&#8595;</div>
    
    <div class="alert alert-warning border-warning py-1 px-3 d-inline-block my-1 fw-bold shadow-sm">
      ⚠️ Common Issue
    </div>
    
    <div class="text-secondary fs-4">&#8595;</div>
    
    <div class="card mx-auto my-2 shadow-sm" style="max-width: 320px;">
      <div class="card-body p-2 bg-white">Fiber Optic Cable</div>
    </div>
    
    <div class="text-secondary fs-4">&#8595;</div>
    
    <div class="card mx-auto my-2 shadow-sm" style="max-width: 320px;">
      <div class="card-body p-2 bg-white">Oil Filled Junction Box</div>
    </div>
  </div>

  <!-- Winch Cable Junction -->
  <div class="my-3 text-center">
    <div class="text-secondary fs-3">&#8595;</div>
    <div class="rounded-circle bg-dark text-white d-flex align-items-center justify-content-center mx-auto my-2 shadow" style="width: 110px; height: 110px; font-weight: bold; font-size: 0.95rem;">
      Winch Cable
    </div>
    <div class="text-secondary fs-3">&#8595;</div>
  </div>

  <!-- Top-side Connections Container -->
  <div class="border border-warning rounded p-4 w-100 position-relative bg-light text-center" style="max-width: 650px; border-style: dashed !important;">
    <span class="badge bg-warning text-dark position-absolute top-0 start-0 translate-middle-y ms-3 fs-6">Top-side Connections</span>
    
    <div class="card mx-auto my-2 shadow-sm" style="max-width: 320px;">
      <div class="card-body p-2 bg-white">Winch Slip Ring</div>
    </div>
    
    <div class="text-secondary fs-4">&#8595;</div>
    
    <div class="alert alert-warning border-warning py-1 px-3 d-inline-block my-1 fw-bold shadow-sm">
      ⚠️ Common Issue
    </div>
    
    <div class="text-secondary fs-4">&#8595;</div>
    
    <div class="card mx-auto my-2 shadow-sm" style="max-width: 320px;">
      <div class="card-body p-2 bg-white">Dry Lab Junction Box</div>
    </div>
    
    <div class="text-secondary fs-4">&#8595;</div>
    
    <div class="alert alert-warning border-warning py-1 px-3 d-inline-block my-1 fw-bold shadow-sm">
      ⚠️ Common Issue
    </div>
    
    <div class="text-secondary fs-4">&#8595;</div>
    
    <div class="card mx-auto my-2 shadow-sm" style="max-width: 320px;">
      <div class="card-body p-2 fw-bold bg-white">Demultiplexer</div>
    </div>
    
    <div class="text-secondary fs-4">&#8595;</div>
    
    <div class="row g-2 justify-content-center mt-3 mb-2">
      <div class="col-auto"><span class="badge bg-secondary p-2">Cam1</span></div>
      <div class="col-auto"><span class="badge bg-secondary p-2">Cam2</span></div>
      <div class="col-auto"><span class="badge bg-secondary p-2">Data Network</span></div>
      <div class="col-auto"><span class="badge bg-secondary p-2">Spare</span></div>
    </div>
  </div>

</div>
```

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
