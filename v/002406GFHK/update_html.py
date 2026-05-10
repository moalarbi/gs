import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Meta
content = content.replace('{{invoice_number}}', '002406')
content = content.replace('{{date}}', '10 مايو 2026')
content = content.replace('{{client_name}}', 'العميل الكريم')
content = content.replace('30 يوم (قابل للتجديد تلقائياً)', '30 يوم')
content = content.replace('إدارة التواجد الرقمي والحملات التسويقية', 'إطلاق وتدشين منصة تعليمية رقمية احترافية')

# Update Hero Description
hero_desc = """<p class="hero-desc" style="margin-top: 15px; font-size: 1.1rem; color: var(--text-secondary); max-width: 600px;">
تصميم متجر إلكتروني احترافي على منصة سلة مع تجهيز مجتمع متدربين خاص وتنظيم الهوية الرقمية لإطلاق المشروع بشكل احترافي ومتوافق مع الجوال.
</p>"""
content = re.sub(r'(<h1 class="hero-title">.*?</h1>)', r'\1\n                    ' + hero_desc, content, flags=re.DOTALL)

# Update Scope Section
new_scope = """
                <div class="scope-grid">
                    <!-- Scope Card 1 -->
                    <div class="scope-card">
                        <div class="scope-header">
                            <span class="scope-icon">🛒</span>
                            <h3 class="scope-title">إنشاء وتدشين المتجر الإلكتروني</h3>
                        </div>
                        <ul class="scope-list">
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تصميم متجر احترافي على منصة سلة</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تجهيز واجهة حديثة ومتوافقة مع الجوال</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">ترتيب صفحات الكورسات والمنتجات</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تجهيز صفحات السياسات والتواصل</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تحسين تجربة المستخدم داخل المتجر</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تجهيز المتجر للإطلاق بشكل احترافي</span></div>
                            </li>
                        </ul>
                    </div>

                    <!-- Scope Card 2 -->
                    <div class="scope-card">
                        <div class="scope-header">
                            <span class="scope-icon">🎨</span>
                            <h3 class="scope-title">إنشاء الهوية الرقمية والسوشيال ميديا</h3>
                        </div>
                        <ul class="scope-list">
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">إنشاء حسابات السوشيال ميديا</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تنسيق الحسابات بشكل احترافي</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">توحيد الهوية البصرية</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تجهيز صور البروفايل والبنرات</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">ربط الحسابات بالمتجر</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تجهيز الشكل العام للبراند</span></div>
                            </li>
                        </ul>
                    </div>

                    <!-- Scope Card 3 -->
                    <div class="scope-card">
                        <div class="scope-header">
                            <span class="scope-icon">👥</span>
                            <h3 class="scope-title">تجهيز مجتمع المتدربين</h3>
                        </div>
                        <ul class="scope-list">
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">إنشاء مجتمع خاص للمتدربين على تيليجرام</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تنظيم صلاحيات الدخول للأعضاء</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">إعداد القنوات والمجموعات بشكل احترافي</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تجهيز نظام مناسب للمحتوى التعليمي المدفوع</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تحسين إدارة الأعضاء والمتدربين</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تسهيل وصول الطلاب للمحتوى</span></div>
                            </li>
                        </ul>
                    </div>

                    <!-- Scope Card 4 -->
                    <div class="scope-card">
                        <div class="scope-header">
                            <span class="scope-icon">🛡️</span>
                            <h3 class="scope-title">الحماية والتنظيم</h3>
                        </div>
                        <ul class="scope-list">
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تنظيم صلاحيات الوصول للمحتوى</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تقييد الوصول للمشتركين فقط</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">إعداد بيئة خاصة للطلاب</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تحسين إدارة الأعضاء</span></div>
                            </li>
                            <li class="scope-item">
                                <span class="item-bullet"></span>
                                <div class="item-content"><span class="item-name">تنظيم تجربة المستخدم داخل المجتمع</span></div>
                            </li>
                        </ul>
                    </div>
                </div>
"""
content = re.sub(r'<div class="scope-grid">.*?</div>\s*</section>', new_scope + '\n            </section>', content, flags=re.DOTALL)

# Update Additional Features (Workflow Section)
new_workflow = """
            <section class="workflow-section">
                <h2 class="section-title">المزايا الإضافية ضمن الاتفاقية</h2>
                <div class="workflow-container">
                    <ul class="workflow-list">
                        <li class="workflow-item">
                            <span class="step-number">1</span>
                            <span class="step-text">متابعة الإطلاق مع الإدارة</span>
                        </li>
                        <li class="workflow-item">
                            <span class="step-number">2</span>
                            <span class="step-text">المساعدة في تنظيم المحتوى</span>
                        </li>
                        <li class="workflow-item">
                            <span class="step-number">3</span>
                            <span class="step-text">استشارة تشغيلية قبل الإطلاق</span>
                        </li>
                        <li class="workflow-item">
                            <span class="step-number">4</span>
                            <span class="step-text">المساعدة في ترتيب رحلة العميل</span>
                        </li>
                    </ul>
                </div>
            </section>
"""
content = re.sub(r'<section class="workflow-section">.*?</section>', new_workflow, content, flags=re.DOTALL)

# Update Pricing
content = content.replace('الاستثمار الشهري', 'تكلفة تأسيس وإطلاق المنصة')
content = content.replace('{{price}}', '2000')
content = content.replace('شهرياً – لمدة 30 يوم – قابل للتجديد تلقائياً', 'يشمل تصميم المتجر، تجهيز المجتمع، إنشاء الحسابات، وتجهيز الهوية الرقمية للإطلاق.')

# Update Exclusions
new_exclusions = """
                <ul class="notes-list">
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">اشتراك منصة سلة</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">الدومين</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">الحملات الإعلانية</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">إنتاج وتصوير الكورسات</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">كتابة المحتوى التعليمي</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">إدارة السوشيال ميديا المستمرة</span></li>
                    <li class="note-item"><span class="note-bullet">•</span><span class="note-text">أي أدوات أو خدمات خارجية مدفوعة</span></li>
                </ul>
"""
content = re.sub(r'<ul class="notes-list">.*?</ul>', new_exclusions, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
