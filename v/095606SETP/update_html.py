import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Meta Information
content = content.replace('{{invoice_number}}', '095606')
content = content.replace('{{date}}', '10 مايو 2026')
content = content.replace('{{client_name}}', 'KIMO PETS')
content = content.replace('30 يوم (قابل للتجديد تلقائياً)', '5 إلى 7 أيام عمل')
content = content.replace('إدارة التواجد الرقمي والحملات التسويقية', 'تجهيز وتدشين متجر KIMO PETS على منصة سلة')

# Update Hero Description
hero_desc = """
                    <p class="hero-desc" style="margin-top: 15px; font-size: 1.1rem; color: var(--text-secondary); max-width: 600px;">
حل متكامل لترتيب وتجهيز متجر متخصص في أكل ومستلزمات القطط، من الهوية والشكل العام إلى الصور والأقسام والبنرات، ليكون المتجر جاهزًا للانطلاق بشكل احترافي ومناسب للجوال.
</p>"""
content = re.sub(r'(<h1 class="hero-title">.*?</h1>)', r'\1\n                    ' + hero_desc, content, flags=re.DOTALL)

# Update Scope Section
new_scope = """
                <div class="scope-grid">
                    <!-- Scope Card 1 -->
                    <div class="scope-card">
                        <div class="scope-header">
                            <span class="scope-icon">✨</span>
                            <h3 class="scope-title">تطوير اسم وهوية المتجر</h3>
                        </div>
                        <ul class="scope-list">
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">اعتماد اسم KIMO PETS كاسم تجاري ألطف وأسهل للحفظ</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">اختيار توجه بصري مناسب لمجال القطط ومستلزماتها</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">اقتراح ألوان وخطوط مناسبة للمتجر</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تجهيز هوية بصرية بسيطة تساعد في ظهور المتجر بشكل احترافي</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">توحيد شكل المتجر بما يناسب البراند</span></div>
                            </li>
                        </ul>
                    </div>

                    <!-- Scope Card 2 -->
                    <div class="scope-card">
                        <div class="scope-header">
                            <span class="scope-icon">🎨</span>
                            <h3 class="scope-title">تجهيز وتصميم واجهة المتجر</h3>
                        </div>
                        <ul class="scope-list">
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">ترتيب الصفحة الرئيسية بشكل احترافي</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تصميم واجهة مناسبة لمتجر متخصص بالقطط</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تجهيز بنرات رئيسية للمتجر</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تحسين تجربة التصفح على الجوال</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">جعل المتجر قريب من ستايل المتاجر المرجعية مثل هوبا وزرفة مع لمسة خاصة لـ KIMO PETS</span></div>
                            </li>
                        </ul>
                    </div>

                    <!-- Scope Card 3 -->
                    <div class="scope-card">
                        <div class="scope-header">
                            <span class="scope-icon">🖼️</span>
                            <h3 class="scope-title">تنسيق المنتجات والصور</h3>
                        </div>
                        <ul class="scope-list">
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">ضبط مقاسات صور المنتجات</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">ترتيب صور المنتجات داخل المتجر</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تحسين طريقة عرض المنتجات</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تنظيم المنتجات داخل الأقسام المناسبة</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">معالجة مشاكل ظهور الصور بشكل غير مرتب</span></div>
                            </li>
                        </ul>
                    </div>

                    <!-- Scope Card 4 -->
                    <div class="scope-card">
                        <div class="scope-header">
                            <span class="scope-icon">🚀</span>
                            <h3 class="scope-title">الإطلاق والمراجعة النهائية</h3>
                        </div>
                        <ul class="scope-list">
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">مراجعة المتجر قبل التسليم</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">اختبار ظهور المتجر على الجوال والكمبيوتر</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">مراجعة الأقسام والبنرات</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">التأكد من وضوح معلومات المتجر</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تسليم المتجر بشكل جاهز للاستخدام</span></div>
                            </li>
                        </ul>
                    </div>
                </div>
"""
content = re.sub(r'<div class="scope-grid">.*?</div>\s*</section>', new_scope + '\n            </section>', content, flags=re.DOTALL)

# Update Additional Features (Workflow Section) to Service Requirements
new_requirements = """
            <section class="workflow-section">
                <h2 class="section-title">متطلبات الخدمة من طرف العميل</h2>
                <div class="workflow-container">
                    <ul class="workflow-list">
                        <li class="workflow-item">
                            <span class="step-number">1</span>
                            <span class="step-text">صلاحية الدخول إلى متجر سلة</span>
                        </li>
                        <li class="workflow-item">
                            <span class="step-number">2</span>
                            <span class="step-text">السجل التجاري أو وثيقة العمل الحر</span>
                        </li>
                        <li class="workflow-item">
                            <span class="step-number">3</span>
                            <span class="step-text">شهادة الآيبان إن وجدت</span>
                        </li>
                        <li class="workflow-item">
                            <span class="step-number">4</span>
                            <span class="step-text">صور المنتجات المتوفرة</span>
                        </li>
                        <li class="workflow-item">
                            <span class="step-number">5</span>
                            <span class="step-text">أسماء المنتجات والأسعار</span>
                        </li>
                        <li class="workflow-item">
                            <span class="step-number">6</span>
                            <span class="step-text">معلومات التواصل الخاصة بالمتجر</span>
                        </li>
                        <li class="workflow-item">
                            <span class="step-number">7</span>
                            <span class="step-text">أي حسابات سوشيال ميديا حالية إن وجدت</span>
                        </li>
                        <li class="workflow-item">
                            <span class="step-number">8</span>
                            <span class="step-text">أي متاجر مرجعية يحب العميل شكلها مثل هوبا أو زرفة</span>
                        </li>
                    </ul>
                </div>
            </section>
"""
content = re.sub(r'<section class="workflow-section">.*?</section>', new_requirements, content, flags=re.DOTALL)

# Update Pricing
content = content.replace('الاستثمار الشهري', 'تكلفة تجهيز وتدشين متجر KIMO PETS')
content = content.replace('{{price}}', '900')
content = content.replace('شهرياً – لمدة 30 يوم – قابل للتجديد تلقائياً', 'يشمل تجهيز شكل المتجر، تنسيق الصور، ترتيب الأقسام، تجهيز البنرات، وتطوير الهوية البصرية البسيطة للانطلاق بشكل احترافي.')

# Add pre-discount price and update pricing display
price_section_pattern = r'(<div class="pricing-amount">\s*<span class="amount">900</span>\s*<span class="currency">ريال سعودي</span>\s*</div>)'
pre_discount_price = """
                    <span class="pricing-label" style="text-decoration: line-through; color: var(--text-secondary);">1500 ريال</span>
"""
content = re.sub(price_section_pattern, pre_discount_price + '\n' + r'\1', content, flags=re.DOTALL)

# Update Exclusions
new_exclusions = """
                <ul class="notes-list">
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">اشتراك منصة سلة</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">شراء الدومين</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">القوالب المدفوعة</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">التطبيقات المدفوعة داخل سلة</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">التصوير الاحترافي للمنتجات</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">كتابة أوصاف طويلة للمنتجات من الصفر</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">الحملات الإعلانية</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">إدارة المتجر بعد التسليم</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">رفع عدد كبير من المنتجات خارج النطاق المتفق عليه</span></li>
                </ul>
"""
content = re.sub(r'<ul class="notes-list">.*?</ul>', new_exclusions, content, flags=re.DOTALL)

# Update website link in footer
content = content.replace('https://matjarak.vercel.app/', 'https://matjarak.vercel.app/') # Ensure it's the correct one
content = content.replace('www.Golf-Studio.umso.co', 'https://matjarak.vercel.app/')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
