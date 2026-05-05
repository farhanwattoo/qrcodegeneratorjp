document.addEventListener('DOMContentLoaded', () => {
    // Theme Switcher
    const themeBtn = document.getElementById('theme-toggle');
    const updateThemeBtn = () => {
        themeBtn.textContent = document.body.getAttribute('data-theme') === 'dark' ? '☀️' : '🌙';
    };

    if (localStorage.getItem('theme') === 'dark') {
        document.body.setAttribute('data-theme', 'dark');
    }
    updateThemeBtn();

    themeBtn.addEventListener('click', () => {
        if (document.body.getAttribute('data-theme') === 'dark') {
            document.body.removeAttribute('data-theme');
            localStorage.setItem('theme', 'light');
        } else {
            document.body.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        }
        updateThemeBtn();
    });

    // Language Dropdown Interactor
    const langSelect = document.getElementById('lang-select');
    if(langSelect) {
        langSelect.addEventListener('change', (e) => {
            const lang = e.target.value;
            window.location.href = `../${lang}/index.html`;
        });
        
        // Auto-select dropdown based on path
        const path = window.location.pathname;
        const matches = path.match(/\/([a-z]{2})\/index\.html/);
        if(matches && matches[1]) {
            langSelect.value = matches[1];
        }
    }

    // Tab Switching Logic
    const tabs = document.querySelectorAll('.tab');
    const panels = document.querySelectorAll('.input-panel');
    let currentType = 'url';

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            panels.forEach(p => p.classList.remove('active'));
            tab.classList.add('active');
            const target = tab.getAttribute('data-target');
            document.getElementById(`panel-${target}`).classList.add('active');
            currentType = target;
            generateQR();
        });
    });

    // Input Selectors
    const inputs = {
        url: document.getElementById('url-input'),
        text: document.getElementById('text-input'),
        email: document.getElementById('email-input'),
        phone: document.getElementById('phone-input'),
        sms_to: document.getElementById('sms-to'),
        sms_msg: document.getElementById('sms-msg'),
        wifi_ssid: document.getElementById('wifi-ssid'),
        wifi_pwd: document.getElementById('wifi-pwd'),
        wifi_enc: document.getElementById('wifi-enc')
    };

    const options = {
        fgColor: document.getElementById('fg-color'),
        bgColor: document.getElementById('bg-color'),
        errorCor: document.getElementById('error-cor'),
        size: document.getElementById('size')
    };

    const canvas = document.getElementById('qrcode-canvas');

    // Binding Live Event Listeners
    Object.values(inputs).forEach(input => {
        if(input) {
            input.addEventListener('input', debounce(generateQR, 300));
        }
    });

    Object.values(options).forEach(opt => {
        if(opt) {
            opt.addEventListener('change', generateQR);
        }
    });

    function debounce(func, wait) {
        let timeout;
        return function(...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), wait);
        };
    }

    // Main QR Generator Logic
    let currentPayload = '';
    function generateQR() {
        let textPayload = '';
        let valid = true;

        if (currentType === 'url') {
            textPayload = inputs.url.value.trim() || 'https://example.com';
        } else if (currentType === 'text') {
            textPayload = inputs.text.value.trim() || 'Sample Text';
        } else if (currentType === 'email') {
            textPayload = `mailto:${inputs.email.value.trim()}`;
        } else if (currentType === 'phone') {
            textPayload = `tel:${inputs.phone.value.trim()}`;
        } else if (currentType === 'sms') {
            textPayload = `smsto:${inputs.sms_to.value.trim()}:${inputs.sms_msg.value.trim()}`;
        } else if (currentType === 'wifi') {
            const ssid = inputs.wifi_ssid.value.trim();
            const pwd = inputs.wifi_pwd.value;
            const enc = inputs.wifi_enc.value;
            textPayload = `WIFI:S:${ssid};T:${enc};P:${pwd};;`;
        }

        // Generate dynamically using qrcode.js (Included natively)
        currentPayload = textPayload;
        renderQRCode(textPayload);
        
        // Hide scan result if user edits
        const scanOverlay = document.getElementById('scan-overlay');
        const scanResult = document.getElementById('scan-result');
        if(scanOverlay) scanOverlay.classList.remove('active');
        if(scanResult) scanResult.classList.remove('active');
    }

    function renderQRCode(text) {
        // Clear canvas
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const size = parseInt(options.size.value, 10);
        canvas.width = size;
        canvas.height = size;

        // Use the global QRCode class
        QRCode.toCanvas(canvas, text, {
            errorCorrectionLevel: options.errorCor.value,
            color: {
                dark: options.fgColor.value,
                light: options.bgColor.value
            },
            width: size,
            margin: 2
        }, function (error) {
            if (error) console.error(error);
        });
    }

    // Download functionality
    document.getElementById('dl-png').addEventListener('click', () => {
        const link = document.createElement('a');
        link.download = 'qrcode.png';
        link.href = canvas.toDataURL("image/png");
        link.click();
    });

    // Scan Simulator
    const simScanBtn = document.getElementById('sim-scan');
    const scanOverlay = document.getElementById('scan-overlay');
    const scanResult = document.getElementById('scan-result');
    
    if(simScanBtn) {
        simScanBtn.addEventListener('click', () => {
            if(!currentPayload) return;
            scanOverlay.classList.add('active');
            scanResult.classList.remove('active');
            
            setTimeout(() => {
                scanOverlay.classList.remove('active');
                scanResult.textContent = `Scanned: ${currentPayload}`;
                scanResult.classList.add('active');
            }, 1500);
        });
    }

    // Initial render
    if(typeof QRCode !== 'undefined') {
        generateQR();
    }

    // Interactive diagram on homepage
    const diagramNodes = document.querySelectorAll('.diagram-node');
    const diagramChips = document.querySelectorAll('.diagram-chip');
    const diagramDetails = document.querySelectorAll('.diagram-detail');
    const activateDiagramStep = (step) => {
        diagramNodes.forEach((el) => el.classList.toggle('is-active', el.dataset.step === step));
        diagramChips.forEach((el) => el.classList.toggle('is-active', el.dataset.step === step));
        diagramDetails.forEach((el) => el.classList.toggle('is-active', el.dataset.step === step));
    };
    diagramNodes.forEach((node) => {
        node.addEventListener('click', () => activateDiagramStep(node.dataset.step));
    });
    diagramChips.forEach((chip) => {
        chip.addEventListener('click', () => activateDiagramStep(chip.dataset.step));
    });
});
