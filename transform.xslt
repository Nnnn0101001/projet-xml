<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" encoding="UTF-8" indent="yes"
    doctype-public="-//W3C//DTD HTML 4.01//EN"/>

  <!-- ============================================================
       TEMPLATE PRINCIPAL
  ============================================================ -->
  <xsl:template match="/">
    <html>
      <head>
        <meta charset="UTF-8"/>
        <title>Rapport d&#8217;Analyse ML &#8211; Supermarché</title>
        <style>
          /* ── Fonts ── */
          @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&amp;family=DM+Mono:wght@400;500&amp;display=swap');

          /* ── Variables ── */
          :root {
            --bg:        #0b0f1a;
            --surface:   #131929;
            --card:      #1a2235;
            --border:    #243048;
            --accent:    #3b82f6;
            --accent2:   #6366f1;
            --danger:    #ef4444;
            --warning:   #f59e0b;
            --success:   #10b981;
            --text:      #e2e8f0;
            --muted:     #64748b;
            --radius:    12px;
          }

          * { box-sizing: border-box; margin: 0; padding: 0; }

          body {
            background: var(--bg);
            color: var(--text);
            font-family: 'DM Mono', monospace;
            font-size: 13px;
            line-height: 1.6;
          }

          /* ── Header ── */
          .header {
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
            border-bottom: 1px solid var(--border);
            padding: 48px 40px 36px;
            position: relative;
            overflow: hidden;
          }
          .header::before {
            content: '';
            position: absolute; inset: 0;
            background: radial-gradient(ellipse 60% 80% at 70% 50%, rgba(99,102,241,.15), transparent);
            pointer-events: none;
          }
          .header h1 {
            font-family: 'Syne', sans-serif;
            font-size: 2.4rem;
            font-weight: 800;
            letter-spacing: -1px;
            background: linear-gradient(90deg, #fff 0%, #a5b4fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
          }
          .header p { color: var(--muted); font-size: 12px; }

          /* ── KPI Cards ── */
          .kpi-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            padding: 32px 40px;
          }
          .kpi {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 20px;
            position: relative;
            overflow: hidden;
          }
          .kpi::after {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 2px;
          }
          .kpi.blue::after  { background: var(--accent); }
          .kpi.indigo::after { background: var(--accent2); }
          .kpi.red::after   { background: var(--danger); }
          .kpi.green::after { background: var(--success); }
          .kpi-label { color: var(--muted); font-size: 11px; text-transform: uppercase; letter-spacing: 1px; }
          .kpi-value { font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; margin: 4px 0; }
          .kpi.blue .kpi-value  { color: var(--accent); }
          .kpi.indigo .kpi-value { color: var(--accent2); }
          .kpi.red .kpi-value   { color: var(--danger); }
          .kpi.green .kpi-value { color: var(--success); }
          .kpi-sub { color: var(--muted); font-size: 11px; }

          /* ── Section ── */
          .section { padding: 0 40px 40px; }
          .section-title {
            font-family: 'Syne', sans-serif;
            font-size: 1rem;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: var(--muted);
            border-left: 3px solid var(--accent);
            padding-left: 12px;
            margin-bottom: 16px;
          }

          /* ── Table ── */
          .table-wrap {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            overflow: hidden;
          }
          .table-controls {
            padding: 16px 20px;
            border-bottom: 1px solid var(--border);
            display: flex;
            gap: 12px;
            align-items: center;
            flex-wrap: wrap;
          }
          .table-controls input, .table-controls select {
            background: var(--surface);
            border: 1px solid var(--border);
            color: var(--text);
            border-radius: 6px;
            padding: 6px 12px;
            font-family: inherit;
            font-size: 12px;
            outline: none;
          }
          .table-controls input:focus, .table-controls select:focus {
            border-color: var(--accent);
          }
          .table-scroll { overflow-x: auto; max-height: 480px; }
          table { width: 100%; border-collapse: collapse; font-size: 12px; }
          thead th {
            background: var(--surface);
            color: var(--muted);
            font-size: 10px;
            letter-spacing: 1px;
            text-transform: uppercase;
            padding: 10px 14px;
            text-align: left;
            position: sticky; top: 0;
            border-bottom: 1px solid var(--border);
            white-space: nowrap;
          }
          tbody tr { border-bottom: 1px solid rgba(36,48,72,.6); transition: background .15s; }
          tbody tr:hover { background: rgba(59,130,246,.05); }
          td { padding: 9px 14px; white-space: nowrap; }

          /* ── Badges ── */
          .badge {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 20px;
            font-size: 10px;
            font-weight: 500;
            letter-spacing: .5px;
          }
          .badge-normal  { background: rgba(16,185,129,.15); color: #6ee7b7; border: 1px solid rgba(16,185,129,.3); }
          .badge-anomalie { background: rgba(239,68,68,.15); color: #fca5a5; border: 1px solid rgba(239,68,68,.3); }
          .badge-petit   { background: rgba(100,116,139,.15); color: #94a3b8; border: 1px solid rgba(100,116,139,.3); }
          .badge-moyen   { background: rgba(59,130,246,.15); color: #93c5fd; border: 1px solid rgba(59,130,246,.3); }
          .badge-gros    { background: rgba(245,158,11,.15); color: #fcd34d; border: 1px solid rgba(245,158,11,.3); }

          /* ── Total color ── */
          .total-high { color: #6ee7b7; font-weight: 500; }
          .total-mid  { color: #93c5fd; }
          .total-low  { color: var(--muted); }

          /* ── Rating bar ── */
          .rating-wrap { display: flex; align-items: center; gap: 6px; }
          .rating-bar  { flex: 1; height: 4px; background: var(--border); border-radius: 2px; min-width: 50px; }
          .rating-fill { height: 100%; border-radius: 2px; background: linear-gradient(90deg, var(--accent2), var(--accent)); }

          /* ── Footer ── */
          .footer {
            margin: 40px;
            padding: 20px;
            border: 1px solid var(--border);
            border-radius: var(--radius);
            color: var(--muted);
            font-size: 11px;
            text-align: center;
          }

          /* ── Pagination ── */
          .pagination {
            padding: 12px 20px;
            border-top: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            color: var(--muted);
            font-size: 11px;
          }
          .pagination button {
            background: var(--surface);
            border: 1px solid var(--border);
            color: var(--text);
            border-radius: 6px;
            padding: 4px 12px;
            font-family: inherit;
            font-size: 11px;
            cursor: pointer;
          }
          .pagination button:hover { border-color: var(--accent); color: var(--accent); }
          .pagination button:disabled { opacity: .3; cursor: default; }
        </style>
      </head>
      <body>

        <!-- ══ HEADER ══ -->
        <div class="header">
          <h1>&#x2728; Rapport d&#8217;Analyse ML</h1>
          <p>Supermarché &#8212; Détection d&#8217;anomalies &#8226; Segmentation clients &#8226; Prédiction des ventes</p>
        </div>

        <!-- ══ KPI ══ -->
        <div class="kpi-grid">
          <div class="kpi blue">
            <div class="kpi-label">Total transactions</div>
            <div class="kpi-value"><xsl:value-of select="count(//Resultat)"/></div>
            <div class="kpi-sub">enregistrements analysés</div>
          </div>
          <div class="kpi red">
            <div class="kpi-label">Anomalies détectées</div>
            <div class="kpi-value"><xsl:value-of select="count(//Resultat[anomalie='Anomalie'])"/></div>
            <div class="kpi-sub">transactions suspectes</div>
          </div>
          <div class="kpi green">
            <div class="kpi-label">Transactions normales</div>
            <div class="kpi-value"><xsl:value-of select="count(//Resultat[anomalie='Normal'])"/></div>
            <div class="kpi-sub">comportement attendu</div>
          </div>
          <div class="kpi indigo">
            <div class="kpi-label">Gros acheteurs</div>
            <div class="kpi-value"><xsl:value-of select="count(//Resultat[nom_segment='Gros acheteur'])"/></div>
            <div class="kpi-sub">segment premium</div>
          </div>
        </div>

        <!-- ══ TABLE ══ -->
        <div class="section">
          <div class="section-title">Détail des transactions</div>
          <div class="table-wrap">
            <div class="table-controls">
              <input type="text" id="searchInput" placeholder="&#128269; Rechercher (ville, produit, ID…)" oninput="filterTable()" style="width:260px"/>
              <select id="anomalieFilter" onchange="filterTable()">
                <option value="">Toutes anomalies</option>
                <option value="Normal">Normal</option>
                <option value="Anomalie">Anomalie</option>
              </select>
              <select id="segmentFilter" onchange="filterTable()">
                <option value="">Tous segments</option>
                <option value="Petit acheteur">Petit acheteur</option>
                <option value="Acheteur moyen">Acheteur moyen</option>
                <option value="Gros acheteur">Gros acheteur</option>
              </select>
              <span id="rowCount" style="color:var(--muted);font-size:11px;margin-left:auto"></span>
            </div>
            <div class="table-scroll">
              <table id="mainTable">
                <thead>
                  <tr>
                    <th>Invoice ID</th>
                    <th>Branche</th>
                    <th>Ville</th>
                    <th>Client</th>
                    <th>Genre</th>
                    <th>Produit</th>
                    <th>Prix unit.</th>
                    <th>Qté</th>
                    <th>Total</th>
                    <th>Date</th>
                    <th>Paiement</th>
                    <th>Rating</th>
                    <th>Anomalie</th>
                    <th>Segment</th>
                  </tr>
                </thead>
                <tbody>
                  <xsl:for-each select="//Resultat">
                    <tr>
                      <td style="color:var(--muted);font-size:11px"><xsl:value-of select="Invoice_ID"/></td>
                      <td><xsl:value-of select="Branch"/></td>
                      <td><xsl:value-of select="City"/></td>
                      <td><xsl:value-of select="Customer_type"/></td>
                      <td><xsl:value-of select="Gender"/></td>
                      <td><xsl:value-of select="Product_line"/></td>
                      <td><xsl:value-of select="Unit_price"/> DH</td>
                      <td><xsl:value-of select="Quantity"/></td>
                      <!-- Couleur conditionnelle sur Total -->
                      <td>
                        <xsl:choose>
                          <xsl:when test="Total &gt; 400">
                            <span class="total-high"><xsl:value-of select="Total"/> DH</span>
                          </xsl:when>
                          <xsl:when test="Total &gt; 150">
                            <span class="total-mid"><xsl:value-of select="Total"/> DH</span>
                          </xsl:when>
                          <xsl:otherwise>
                            <span class="total-low"><xsl:value-of select="Total"/> DH</span>
                          </xsl:otherwise>
                        </xsl:choose>
                      </td>
                      <td><xsl:value-of select="Date"/></td>
                      <td><xsl:value-of select="Payment"/></td>
                      <!-- Barre de rating -->
                      <td>
                        <div class="rating-wrap">
                          <span><xsl:value-of select="Rating"/></span>
                          <div class="rating-bar">
                            <div class="rating-fill">
                              <xsl:attribute name="style">
                                width:<xsl:value-of select="Rating * 10"/>%
                              </xsl:attribute>
                            </div>
                          </div>
                        </div>
                      </td>
                      <!-- Badge anomalie -->
                      <td>
                        <xsl:choose>
                          <xsl:when test="anomalie='Anomalie'">
                            <span class="badge badge-anomalie">&#9888; Anomalie</span>
                          </xsl:when>
                          <xsl:otherwise>
                            <span class="badge badge-normal">&#10003; Normal</span>
                          </xsl:otherwise>
                        </xsl:choose>
                      </td>
                      <!-- Badge segment -->
                      <td>
                        <xsl:choose>
                          <xsl:when test="nom_segment='Gros acheteur'">
                            <span class="badge badge-gros"><xsl:value-of select="nom_segment"/></span>
                          </xsl:when>
                          <xsl:when test="nom_segment='Acheteur moyen'">
                            <span class="badge badge-moyen"><xsl:value-of select="nom_segment"/></span>
                          </xsl:when>
                          <xsl:otherwise>
                            <span class="badge badge-petit"><xsl:value-of select="nom_segment"/></span>
                          </xsl:otherwise>
                        </xsl:choose>
                      </td>
                    </tr>
                  </xsl:for-each>
                </tbody>
              </table>
            </div>
            <div class="pagination">
              <button id="prevBtn" onclick="changePage(-1)">&#8592; Précédent</button>
              <span id="pageInfo"></span>
              <button id="nextBtn" onclick="changePage(1)">Suivant &#8594;</button>
            </div>
          </div>
        </div>

        <!-- ══ FOOTER ══ -->
        <div class="footer">
          Rapport généré automatiquement par transformation XSLT &#8212;
          Modèles ML : IsolationForest (anomalies) &#8226; RandomForestRegressor (prédiction) &#8226; KMeans (segmentation)
        </div>

        <!-- ══ JS : filtre + pagination ══ -->
        <script>
          const ROWS_PER_PAGE = 25;
          let currentPage = 1;
          let visibleRows = [];

          function getAllRows() {
            return Array.from(document.querySelectorAll('#mainTable tbody tr'));
          }

          function filterTable() {
            const search   = document.getElementById('searchInput').value.toLowerCase();
            const anomalie = document.getElementById('anomalieFilter').value;
            const segment  = document.getElementById('segmentFilter').value;

            visibleRows = getAllRows().filter(row => {
              const text = row.textContent.toLowerCase();
              const cells = row.querySelectorAll('td');
              const rowAnomalie = cells[12] ? cells[12].textContent.trim() : '';
              const rowSegment  = cells[13] ? cells[13].textContent.trim() : '';

              const matchSearch  = !search  || text.includes(search);
              const matchAnomalie = !anomalie || rowAnomalie.includes(anomalie);
              const matchSegment  = !segment  || rowSegment.includes(segment);
              return matchSearch &amp;&amp; matchAnomalie &amp;&amp; matchSegment;
            });

            currentPage = 1;
            renderPage();
          }

          function renderPage() {
            const all = getAllRows();
            all.forEach(r => r.style.display = 'none');

            const start = (currentPage - 1) * ROWS_PER_PAGE;
            const end   = start + ROWS_PER_PAGE;
            visibleRows.slice(start, end).forEach(r => r.style.display = '');

            const total = visibleRows.length;
            const pages = Math.ceil(total / ROWS_PER_PAGE) || 1;
            document.getElementById('pageInfo').textContent =
              `Page ${currentPage} / ${pages}  (${total} résultats)`;
            document.getElementById('rowCount').textContent =
              `${total} ligne${total > 1 ? 's' : ''}`;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage >= pages;
          }

          function changePage(dir) {
            currentPage += dir;
            renderPage();
          }

          // Init
          visibleRows = getAllRows();
          renderPage();
        </script>

      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
