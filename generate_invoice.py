import os
import re

def generate_invoice():
    print("\n--- إنشاء فاتورة جديدة ---")

    invoice_number = input("أدخل رقم الفاتورة (مثال: 002400): ")
    random_code = input("أدخل كود عشوائي مكون من 6 أحرف (بدون O و I وبدون أرقام، مثال: ABCDEF): ").upper()
    client_name = input("أدخل اسم العميل (مثال: شركة العميل المحدودة): ")
    date = input("أدخل تاريخ الفاتورة (مثال: ٥-٣-٢٠٢٦): ")
    duration = input("أدخل مدة التنفيذ (مثال: 20 يوم): ")
    total_price = input("أدخل السعر الإجمالي (مثال: 2500 ريال سعودي): ")

    folder_name = f"{invoice_number}{random_code}"
    invoice_path = f"v/{folder_name}/index.html"
    full_path = os.path.join(os.getcwd(), invoice_path)

    # Read the template content
    # Assuming the script is run from the root of the gs_manual repository
    template_content = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>فاتورة اتفاقية - RAHA Health</title>

    <!-- Google Fonts - IBM Plex Sans Arabic -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <!-- External Libraries -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

    <!-- Styles -->
    <link rel="stylesheet" href="../../assets/style.css">
    <style>
        .toast {
            visibility: hidden;
            min-width: 200px;
            background-color: #333;
            color: #fff;
            text-align: center;
            border-radius: 8px;
            padding: 12px;
            position: fixed;
            z-index: 1000;
            left: 50%;
            bottom: 30px;
            transform: translateX(-50%);
            font-size: 14px;
        }
        .toast.show {
            visibility: visible;
            animation: fadein 0.5s, fadeout 0.5s 2.5s;
        }
        @keyframes fadein { from {bottom: 0; opacity: 0;} to {bottom: 30px; opacity: 1;} }
        @keyframes fadeout { from {bottom: 30px; opacity: 1;} to {bottom: 0; opacity: 0;} }
    </style>
</head>
<body>
    <!-- Toast Notification -->
    <div id="toast" class="toast">تم نسخ الرابط بنجاح</div>

    <!-- Top Bar -->
    <header class="top-bar no-print">
        <div class="top-bar-content">
            <div class="brand">
                <span class="brand-icon">🩺</span>
                <span class="brand-name">RAHA HEALTH</span>
            </div>
        </div>
    </header>

    <!-- Main Document Card -->
    <main class="document-wrapper">
        <div class="document-card" id="document-card">

            <!-- Hero Section -->
            <section class="hero-section">
                <div class="hero-banner">
                    <h1 class="hero-title">
                        <span>فاتورة اتفاقية</span><br>
                        تطوير متجر خدمات طبية متكامل
                    </h1>
                </div>
            </section>

            <!-- Invoice Meta Section -->
            <section class="meta-section">
                <div class="meta-single-card">
                    <div class="meta-row">
                        <span class="meta-label">رقم الفاتورة:</span>
                        <span class="meta-value" id="invoice-number">002399</span>
                    </div>
                    <div class="meta-row">
                        <span class="meta-label">تاريخ الفاتورة:</span>
                        <span class="meta-value">٢-٣-٢٠٢٦</span>
                    </div>
                    <div class="meta-row">
                        <span class="meta-label">المقدمة إلى:</span>
                        <span class="meta-value company-name">ادارة مركز رها للرعاية الطبيه</span>
                    </div>
                    <div class="meta-row">
                        <span class="meta-label">مدة التنفيذ:</span>
                        <span class="meta-value">14 يوم</span>
                    </div>
                </div>
            </section>

            <!-- Scope Section -->
            <section class="scope-section">
                <h2 class="section-title">بنود الاتفاقية</h2>

                <div class="scope-grid">
                    <!-- Scope Card 1 -->
                    <div class="scope-card">
                        <div class="scope-header">
                            <span class="scope-icon">🎨</span>
                            <h3 class="scope-title">تصميم وتجربة المستخدم (UI/UX)</h3>
                        </div>
                        <ul class="scope-list">
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content">
                                    <span class="item-name">تصميم واجهة احترافية متجاوبة (جوال – تابلت – كمبيوتر)</span>
                                </div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content">
                                    <span class="item-name">تحسين رحلة العميل: خدمة → حجز → دفع</span>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <!-- Scope Card 2 -->
                    <div class="scope-card">
                        <div class="scope-header">
                            <span class="scope-icon">🛍️</span>
                            <h3 class="scope-title">إعداد متجر سلة وهيكلة الخدمات</h3>
                        </div>
                        <ul class="scope-list">
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content">
                                    <span class="item-name">تهيئة الخدمات كمنتجات قابلة للبيع + تصنيفات واضحة</span>
                                </div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content">
                                    <span class="item-name">تفعيل القسائم والعروض + إعدادات خدمة العملاء</span>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <!-- Scope Card 3 -->
                    <div class="scope-card">
                        <div class="scope-header">
                            <span class="scope-icon">📅</span>
                            <h3 class="scope-title">الحجز والدفع وتهيئة SEO</h3>
                        </div>
                        <ul class="scope-list">
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content">
                                    <span class="item-name">تفعيل نظام الحجز واختيار الوقت للخدمات المنزلية</span>
                                </div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content">
                                    <span class="item-name">ربط بوابات الدفع الإلكتروني حسب تفعيل الحساب</span>
                                </div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content">
                                    <span class="item-name">إعداد SEO أساسي + ربط Analytics / Search Console</span>
                                </div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content">
                                    <span class="item-name">تهيئة الأمان والصفحات النظامية + اختبار قبل التسليم</span>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- Workflow Section -->
            <section class="workflow-section">
                <h2 class="section-title">آلية العمل</h2>
                <div class="workflow-container">
                    <ul class="workflow-list">
                        <li class="workflow-item"><span class="step-number">1</span><span class="step-text">استلام المتطلبات وتأكيد الخدمات</span></li>
                        <li class="workflow-item"><span class="step-number">2</span><span class="step-text">تصميم الواجهة وتجهيز الصفحات</span></li>
                        <li class="workflow-item"><span class="step-number">3</span><span class="step-text">إعداد متجر سلة + الحجز + الدفع</span></li>
                        <li class="workflow-item"><span class="step-number">4</span><span class="step-text">SEO + التحليلات + الاختبار</span></li>
                        <li class="workflow-item"><span class="step-number">5</span><span class="step-text">التسليم والتدريب المختصر</span></li>
                    </ul>
                    <div class="workflow-note">
                        <span class="highlight-text">مدة التنفيذ: 14 يوم</span>
                    </div>
                </div>
            </section>

            <!-- Pricing Section -->
            <section class="pricing-section">
                <div class="pricing-box">
                    <span class="pricing-label">قيمة المشروع</span>
                    <div class="pricing-amount">
                        <span class="amount">1,876</span>
                        <span class="currency">ريال سعودي</span>
                    </div>
                    <p class="pricing-note">قيمة إجمالية – تُسلم خلال 14 يوم</p>
                </div>
            </section>

            <!-- Notes Section -->
            <section class="notes-section">
                <h2 class="section-title">ملاحظات</h2>
                <ul class="notes-list">
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">التنفيذ ضمن إمكانيات منصة سلة والإضافات المتاحة.</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">أي تطويرات خاصة خارج نطاق سلة تعتبر أعمال إضافية.</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">الميزانيات الإعلانية غير مشمولة.</span></li>
                </ul>
            </section>

            <!-- Footer -->
            <footer class="document-footer">
                <div class="footer-content">
                    <div class="footer-brand">
                        <span class="footer-brand-name">GOLF STUDIO</span>
                    </div>
                    <div class="footer-contact">
                        <a href="https://wa.me/966537311886" target="_blank" class="contact-item">
                            <span class="contact-icon">📞</span>
                            0537311886
                        </a>
                        <a href="mailto:Golf.Studio.Adv@gmail.com" class="contact-item">
                            <span class="contact-icon">✉️</span>
                            Golf.Studio.Adv@gmail.com
                        </a>
                        <a href="https://golf-stusio.umso.co/" target="_blank" class="contact-item">
                            <span class="contact-icon">🌐</span>
                            www.Golf-Studio.umso.co
                        </a>
                    </div>
                </div>
                <div class="print-action-bottom no-print">
                    <button class="btn btn-primary btn-large" onclick="copyInvoiceLink()">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-left: 8px;">
                            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                        </svg>
                        نسخ رابط الفاتورة
                    </button>
                </div>
            </footer>

        </div>
    </main>

    <!-- Scripts -->
    <script src="../../assets/script.js"></script>
    <script>
        function copyInvoiceLink() {
            const url = window.location.href;
            navigator.clipboard.writeText(url).then(() => {
                const toast = document.getElementById("toast");
                toast.className = "toast show";
                setTimeout(() => { toast.className = toast.className.replace("show", ""); }, 3000);
            }).catch(err => {
                console.error(\'Failed to copy: \', err);
            });
        }
    </script>
</body>
</html>
    """

    # Replace placeholders
    content = template_content.replace("002399", invoice_number)
    content = content.replace("٢-٣-٢٠٢٦", date)
    content = content.replace("ادارة مركز رها للرعاية الطبيه", client_name)
    content = content.replace("14 يوم", duration)
    content = content.replace("1,876", total_price)
    content = content.replace("RAHA HEALTH", "GOLF STUDIO") # Ensure brand name is GOLF STUDIO
    content = re.sub(r'<span class="item-count">\(.*\)</span>', '', content) # Remove individual prices
    content = content.replace("https://wa.me/966537311886", f"https://wa.me/966{re.sub(r'[^0-9]', '', input('أدخل رقم الواتساب (مثال: 0537311886): '))}") # WhatsApp number
    content = content.replace("https://golf-stusio.umso.co/", input("أدخل رابط الموقع (مثال: https://golf-stusio.umso.co/): ")) # Website link

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # Write the new invoice file
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\nتم إنشاء الفاتورة بنجاح في: {full_path}")
    print(f"الرابط المتوقع: https://moalarbi.github.io/gs/{invoice_path}")

if __name__ == "__main__":
    generate_invoice()
