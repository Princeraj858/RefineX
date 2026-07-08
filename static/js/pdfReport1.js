// =============================================
// RefineX Professional PDF Generator
// =============================================

const { jsPDF } = window.jspdf;

const BRAND = {
    blue:[13,71,161],
    green:[40,167,69],
    orange:[255,152,0],
    red:[220,53,69],
    black:[40,40,40],
    gray:[120,120,120]
};

function value(id){

    const e=document.getElementById(id);

    if(!e) return "--";

    return e.innerText.trim();

}

function reportData(report = null){

    if(report){

        return{
            equipmentName: report.equipment_name,
            equipmentId: report.equipment_id,
            category: report.category,
            manufacturer: report.manufacturer,
            unit: report.unit,
            section: report.section,
            prediction: report.prediction,
            confidence: report.confidence + "%",
            failure: report.failure_probability + "%",
            rul: report.remaining_life,
            action: report.recommended_action,
            temperature: report.temperature,
            pressure: report.pressure,
            vibration: report.vibration,
            hours: report.operating_hours,
            temperatureStatus: report.sensor_status.temperature,
            pressureStatus: report.sensor_status.pressure,
            vibrationStatus: report.sensor_status.vibration,
            image: report.image_path
        };

    }

    return {
        equipmentName:value("reportEquipmentName"),
        equipmentId:value("reportEquipmentId"),
        category:value("reportCategory"),
        manufacturer:value("reportManufacturer"),
        unit:value("reportUnit"),
        section:value("reportSection"),
        prediction:value("statusBadge"),
        confidence:value("confidence"),
        failure:value("failureProbability"),
        rul:value("rul"),
        action:value("action"),
        temperature:value("reportTemperature"),
        pressure:value("reportPressure"),
        vibration:value("reportVibration"),
        hours:value("reportHours"),
        temperatureStatus:value("reportTemperatureStatus"),
        pressureStatus:value("reportPressureStatus"),
        vibrationStatus:value("reportVibrationStatus"),
        image:document.getElementById("reportImage")?.src || ""
    };

}   

function reportHeader(pdf){

    pdf.setFillColor(13,71,161);

    pdf.rect(0,0,210,28,"F");

    pdf.setTextColor(255,255,255);

    pdf.setFont("helvetica","bold");

    pdf.setFontSize(22);

    pdf.text("RefineX AI",14,13);

    pdf.setFontSize(11);

    pdf.setFont("helvetica","normal");

    pdf.text(
        "Smart Predictive Maintenance Report",
        14,
        20
    );

    pdf.setFontSize(9);

    pdf.text(

        new Date().toLocaleString(),

        150,

        20

    );

}

function healthColor(status){

    status=status.toLowerCase();

    if(status.includes("healthy"))

        return [40,167,69];

    if(status.includes("warning"))

        return [255,152,0];

    return [220,53,69];

}

function drawPredictionBadge(pdf,status,y){

    const c=healthColor(status);

    pdf.setFillColor(c[0],c[1],c[2]);

    pdf.roundedRect(

        150,

        y-5,

        40,

        8,

        2,

        2,

        "F"

    );

    pdf.setTextColor(255,255,255);

    pdf.setFontSize(10);

    pdf.setFont("helvetica","bold");

    pdf.text(

        status,

        170,

        y,

        {

            align:"center"

        }

    );

    pdf.setTextColor(0,0,0);

}

async function generatePDF(report = null){
    try{
    
        const data = reportData(report);    
    const pdf = new jsPDF("p","mm","a4");
    
    reportHeader(pdf);
    
    // =========================
    // Equipment Information
    // =========================
    
    pdf.autoTable({
    
    startY:38,
    
    theme:"grid",
    
    styles:{
    
    fontSize:10,
    
    cellPadding:3
    
    },
    
    headStyles:{
    
    fillColor:[13,71,161],
    
    textColor:255,
    
    fontStyle:"bold"
    
    },
    
    head:[
    
    ["Equipment Information","Value"]
    
    ],
    
    body:[
    
    ["Equipment Name",data.equipmentName],
    
    ["Equipment ID",data.equipmentId],
    
    ["Category",data.category],
    
    ["Manufacturer",data.manufacturer],
    
    ["Unit",data.unit],
    
    ["Section",data.section]
    
    ]
    
    });
    
    
    // =========================
    // AI Prediction
    // =========================
    
    let y = pdf.lastAutoTable.finalY + 8;
    
    pdf.autoTable({
    
    startY:y,
    
    theme:"grid",
    
    styles:{
    
    fontSize:10,
    
    cellPadding:3
    
    },
    
    headStyles:{
    
    fillColor:[13,71,161],
    
    textColor:255
    
    },
    
    head:[
    
    ["AI Prediction","Result"]
    
    ],
    
    body:[
    
    ["Health Status",data.prediction],
    
    ["Confidence",data.confidence],
    
    ["Failure Probability",data.failure],
    
    ["Remaining Useful Life",data.rul],
    
    ["Recommended Action",data.action]
    
    ]
    
    });
    
    y = pdf.lastAutoTable.finalY + 6;
    
    // nice coloured badge
    
    drawPredictionBadge(
    
    pdf,
    
    data.prediction,
    
    y
    
    );
// =========================
// Sensor Readings
// =========================

y += 10;

pdf.autoTable({

startY:y,

theme:"grid",

styles:{

fontSize:10,

cellPadding:3

},

headStyles:{

fillColor:[13,71,161],

textColor:255

},

head:[

["Sensor","Current Reading"]

],

body:[

["Temperature",data.temperature],

["Pressure",data.pressure],

["Vibration",data.vibration],

["Operating Hours",data.hours]

]

});


// =========================
// Sensor Status
// =========================

y = pdf.lastAutoTable.finalY + 8;

pdf.autoTable({

startY:y,

theme:"grid",

styles:{

fontSize:10,

cellPadding:3

},

headStyles:{

fillColor:[13,71,161],

textColor:255

},

head:[

["Sensor","Status"]

],

body:[

["Temperature",data.temperatureStatus],

["Pressure",data.pressureStatus],

["Vibration",data.vibrationStatus]

]

});

y = pdf.lastAutoTable.finalY + 10;
// ======================================
// Equipment Image
// ======================================

if(data.image && data.image !== ""){

    try{

        if(y > 220){

            pdf.addPage();

            y = 20;

        }

        pdf.setFillColor(13,71,161);

        pdf.rect(14,y,182,8,"F");

        pdf.setTextColor(255,255,255);

        pdf.setFontSize(11);

        pdf.setFont("helvetica","bold");

        pdf.text("Equipment Image",18,y+5);

        y += 12;

        const img = new Image();

img.crossOrigin = "Anonymous";

let imageUrl = data.image || "";

// Convert Windows path to browser path
imageUrl = imageUrl.replace(/\\/g, "/");

// If only uploads/... is stored, prepend backend URL
if (
    imageUrl &&
    !imageUrl.startsWith("http")
) {
    imageUrl = `${window.location.origin}/${imageUrl}`;
}

console.log("Loading image:", imageUrl);

img.src = imageUrl;

await new Promise((resolve, reject) => {
    img.onload = resolve;
    img.onerror = reject;
});
        pdf.addImage(

            img,

            "JPEG",

            45,

            y,

            120,

            70

        );

        y += 80;

    }

    catch(err){

        console.log("Image skipped");

    }

}
// ======================================
// AI Recommendation Box
// ======================================

if(y > 235){

    pdf.addPage();

    y = 20;

}

pdf.setFillColor(245,247,250);

pdf.roundedRect(

14,

y,

182,

26,

3,

3,

"F"

);

pdf.setDrawColor(13,71,161);

pdf.roundedRect(

14,

y,

182,

26,

3,

3

);

pdf.setTextColor(13,71,161);

pdf.setFont("helvetica","bold");

pdf.setFontSize(11);

pdf.text(

"AI Recommendation",

18,

y+7

);

pdf.setTextColor(40,40,40);

pdf.setFont("helvetica","normal");

pdf.setFontSize(10);

pdf.text(

data.action,

18,

y+16,

{

maxWidth:170

}

);

y += 40;
// ======================================
// Footer
// ======================================

pdf.setDrawColor(180);

pdf.line(

14,

285,

196,

285

);

pdf.setFontSize(8);

pdf.setTextColor(120);

pdf.text(

"Generated by RefineX AI",

14,

290

);

pdf.text(

"Indian Oil Corporation Limited",

70,

290

);

pdf.text(

"Guwahati Refinery",

150,

290

);

pdf.setFontSize(8);

pdf.text(

"Report ID : RX-"+Date.now(),

14,

295

);

pdf.text(

new Date().toLocaleString(),

135,

295

);
// ======================================
// Page Number
// ======================================

const totalPages = pdf.internal.getNumberOfPages();

for(let i=1;i<=totalPages;i++){

    pdf.setPage(i);

    pdf.setFontSize(8);

    pdf.setTextColor(120);

    pdf.text(

        `Page ${i} of ${totalPages}`,

        195,

        290,

        {align:"right"}

    );

}

// ======================================
// Save PDF
// ======================================

const filename =

`RefineX_Report_${data.equipmentId}_${new Date()
.toISOString()
.slice(0,10)}.pdf`;

console.log("Saving PDF...");

pdf.save(filename);

console.log("PDF Saved Successfully.");

}

catch(err){

    console.error("PDF ERROR :",err);

    alert(

        "Unable to generate report.\n\n"+

        err.message

    );

}

}

// ======================================
// Download Button
// ======================================

document.addEventListener("DOMContentLoaded",()=>{

    const btn=document.getElementById("downloadReportBtn");

    if(btn){

        btn.addEventListener("click",()=>{

            generatePDF();

        });

    }

});