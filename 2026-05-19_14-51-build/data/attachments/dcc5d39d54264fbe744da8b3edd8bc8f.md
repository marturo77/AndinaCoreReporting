# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: reservas\notas_tecnicas.feature.spec.js >> R32 Notas Tecnicas >> R32-C03 verificar archivos cargados de nota tecnica
- Location: .features-gen\reservas\notas_tecnicas.feature.spec.js:23:7

# Error details

```
TimeoutError: page.waitForEvent: Timeout 12000ms exceeded while waiting for event "download"
=========================== logs ===========================
waiting for event "download"
============================================================
```

# Page snapshot

```yaml
- generic [ref=e1]:
  - generic [ref=e3]:
    - banner [ref=e5]:
      - generic [ref=e6]:
        - generic [ref=e10]:
          - generic [ref=e12]: search
          - generic [ref=e13]:
            - searchbox "Buscar" [ref=e14]
            - generic: Buscar
        - generic [ref=e15]:
          - generic [ref=e16]:
            - button [ref=e17] [cursor=pointer]:
              - img [ref=e19]: notifications
            - button [ref=e20] [cursor=pointer]:
              - img [ref=e22]: help
            - button [ref=e23] [cursor=pointer]:
              - img [ref=e25]: settings
          - generic [ref=e29] [cursor=pointer]:
            - generic [ref=e30]:
              - figure "Avatar de Marcelo Arturo Duarte Duarte" [ref=e31]: M
              - generic [ref=e33]: Marcelo Arturo Duarte Duarte
            - combobox "Avatar de Marcelo Arturo Duarte Duarte Marcelo Arturo Duarte Duarte" [ref=e34]
            - generic [ref=e36]: expand_more
    - complementary [ref=e37]:
      - generic [ref=e38]:
        - img [ref=e39]:
          - img [ref=e41]
        - paragraph [ref=e45] [cursor=pointer]:
          - generic [ref=e46]: home
          - text: Inicio
        - generic [ref=e47]:
          - generic [ref=e50] [cursor=pointer]:
            - paragraph [ref=e51]:
              - generic [ref=e52]: wallet
              - text: Cartera
            - generic [ref=e53]: keyboard_arrow_down
          - generic:
            - generic [ref=e56] [cursor=pointer]: Generar Reporte de Conciliación de recaudos
            - generic [ref=e59] [cursor=pointer]: Aplicación de Recaudo
        - generic [ref=e60]:
          - generic [ref=e63] [cursor=pointer]:
            - paragraph [ref=e64]:
              - generic [ref=e65]: account_balance_wallet
              - text: Suscripción y cotización
            - generic [ref=e66]: keyboard_arrow_down
          - generic:
            - generic [ref=e69] [cursor=pointer]: Crear Cotización
            - generic [ref=e72] [cursor=pointer]: Consulta cotización
            - generic [ref=e75] [cursor=pointer]: Beneficiarios cotización
            - generic [ref=e77] [cursor=pointer]:
              - paragraph [ref=e78]: Reporte respuesta cotización AFP
              - generic [ref=e79]: keyboard_arrow_down
        - generic [ref=e80]:
          - generic [ref=e83] [cursor=pointer]:
            - paragraph [ref=e84]:
              - generic [ref=e85]: article
              - text: Emisión
            - generic [ref=e86]: keyboard_arrow_down
          - generic:
            - generic [ref=e89] [cursor=pointer]: Kit de Bienvenida
            - generic [ref=e92] [cursor=pointer]: Emisión de Pólizas
            - generic [ref=e95] [cursor=pointer]: Consulta de pólizas emitidas
            - generic [ref=e98] [cursor=pointer]: Consulta de pólizas
        - generic [ref=e99]:
          - generic [ref=e102] [cursor=pointer]:
            - paragraph [ref=e103]:
              - generic [ref=e104]: layers
              - text: Integraciones
            - generic [ref=e105]: keyboard_arrow_down
          - generic:
            - generic [ref=e107] [cursor=pointer]:
              - paragraph [ref=e108]:
                - generic [ref=e109]: swap_vertical_circle
                - text: Integración Nómina
              - generic [ref=e110]: keyboard_arrow_down
            - generic [ref=e112] [cursor=pointer]:
              - paragraph [ref=e113]:
                - generic [ref=e114]: swap_vertical_circle
                - text: Integración ERP
              - generic [ref=e115]: keyboard_arrow_down
            - generic [ref=e117] [cursor=pointer]:
              - paragraph [ref=e118]:
                - generic [ref=e119]: swap_vertical_circle
                - text: Integración OBP
              - generic [ref=e120]: keyboard_arrow_down
            - generic [ref=e122] [cursor=pointer]:
              - paragraph [ref=e123]:
                - generic [ref=e124]: swap_vertical_circle
                - text: Integración CRM
              - generic [ref=e125]: keyboard_arrow_down
        - generic [ref=e126]:
          - generic [ref=e129] [cursor=pointer]:
            - paragraph [ref=e130]:
              - generic [ref=e131]: request_quote
              - text: Facturación
            - generic [ref=e132]: keyboard_arrow_down
          - generic:
            - generic [ref=e135] [cursor=pointer]: Generar facturas
            - generic [ref=e138] [cursor=pointer]: Reporte facturas
            - generic [ref=e141] [cursor=pointer]: Administración consecutivos de resolución DIAN
            - generic [ref=e144] [cursor=pointer]: Reporte de errores de facturación
        - generic [ref=e145]:
          - generic [ref=e148] [cursor=pointer]:
            - paragraph [ref=e149]:
              - generic [ref=e150]: file_copy
              - text: Administración de pólizas
            - generic [ref=e151]: keyboard_arrow_down
          - generic:
            - generic [ref=e154] [cursor=pointer]: Lista de pólizas
            - generic [ref=e157] [cursor=pointer]: Aprobación de novedades
            - generic [ref=e160] [cursor=pointer]: Consulta de novedades
        - generic [ref=e161]:
          - generic [ref=e164] [cursor=pointer]:
            - paragraph [ref=e165]:
              - generic [ref=e166]: person_outline
              - text: Siniestros
            - generic [ref=e167]: keyboard_arrow_down
          - generic:
            - generic [ref=e170] [cursor=pointer]: Crear siniestro
            - generic [ref=e173] [cursor=pointer]: Consultar Siniestros
            - generic [ref=e176] [cursor=pointer]: Trámites en gestión
            - generic [ref=e179] [cursor=pointer]: Pagos de siniestros
            - generic [ref=e182] [cursor=pointer]: Pagos
            - generic [ref=e185] [cursor=pointer]: Consulta de órdenes de Pago
            - generic [ref=e188] [cursor=pointer]: Reporte de comunicaciones
        - generic [ref=e189]:
          - generic [ref=e192] [cursor=pointer]:
            - paragraph [ref=e193]:
              - generic [ref=e194]: tune
              - text: Reservas
            - generic [ref=e195]: keyboard_arrow_down
          - generic:
            - generic [ref=e198] [cursor=pointer]: Reserva Matemática
            - generic [ref=e201] [cursor=pointer]: Consulta Histórica
        - generic [ref=e202]:
          - generic [ref=e205] [cursor=pointer]:
            - paragraph [ref=e206]:
              - generic [ref=e207]: settings
              - text: Parámetros
            - generic [ref=e208]: keyboard_arrow_up
          - generic [ref=e209]:
            - generic [ref=e211] [cursor=pointer]:
              - paragraph [ref=e212]: Generales
              - generic [ref=e213]: keyboard_arrow_down
            - generic [ref=e215] [cursor=pointer]:
              - paragraph [ref=e216]: Producto
              - generic [ref=e217]: keyboard_arrow_down
        - generic [ref=e218]:
          - generic [ref=e221] [cursor=pointer]:
            - paragraph [ref=e222]:
              - generic [ref=e223]: layers
              - text: Reportes
            - generic [ref=e224]: keyboard_arrow_down
          - generic:
            - generic [ref=e226] [cursor=pointer]:
              - paragraph [ref=e227]: Reportes SFC
              - generic [ref=e228]: keyboard_arrow_down
            - generic [ref=e231] [cursor=pointer]: Reporte de pólizas y beneficiarios
            - generic [ref=e233] [cursor=pointer]:
              - paragraph [ref=e234]: Endosos y carátulas
              - generic [ref=e235]: keyboard_arrow_down
            - generic [ref=e238] [cursor=pointer]: Informe RNBD
            - generic [ref=e241] [cursor=pointer]: Reporte de Nomina
            - generic [ref=e244] [cursor=pointer]: Informes OBP
    - main [ref=e246]:
      - generic [ref=e249]:
        - generic [ref=e251]: settings
        - heading "Parámetros de producto" [level=1] [ref=e253]
      - generic "PARAMETROS_PRODUCTO" [ref=e254]:
        - generic [ref=e256]:
          - generic [ref=e259]:
            - 'heading "Tipo de Variable: Nota Técnica" [level=5] [ref=e260]'
            - generic [ref=e262]:
              - button "Atras" [ref=e263] [cursor=pointer]:
                - generic [ref=e265]: Atras
              - button "Agregar" [ref=e266] [cursor=pointer]:
                - generic [ref=e268]: Agregar
          - table [ref=e270]:
            - rowgroup [ref=e271]:
              - row "Periodo Valor Fecha inicio vigencia Fecha fin vigencia Acciones" [ref=e272]:
                - columnheader "Periodo" [ref=e273]
                - columnheader "Valor" [ref=e274]
                - columnheader "Fecha inicio vigencia" [ref=e275]
                - columnheader "Fecha fin vigencia" [ref=e276]
                - columnheader "Acciones" [ref=e277]
            - rowgroup [ref=e278]:
              - row "2027-1 29/11/2024-1436-NT-P-40-0000000000000001 01/01/2027 31/12/2027" [ref=e279]:
                - cell "2027-1" [ref=e280]
                - cell "29/11/2024-1436-NT-P-40-0000000000000001" [ref=e281]
                - cell "01/01/2027" [ref=e282]
                - cell "31/12/2027" [ref=e283]
                - cell [ref=e284]:
                  - button [ref=e286] [cursor=pointer]:
                    - img [ref=e288]: edit
              - row "2025 29/11/2024-1436-NT-P-40-0000000000000001 01/01/2025 31/12/2026" [ref=e289]:
                - cell "2025" [ref=e290]
                - cell "29/11/2024-1436-NT-P-40-0000000000000001" [ref=e291]
                - cell "01/01/2025" [ref=e292]
                - cell "31/12/2026" [ref=e293]
                - cell [ref=e294]:
                  - button [ref=e296] [cursor=pointer]:
                    - img [ref=e298]: edit
        - generic [ref=e299]:
          - generic [ref=e300]:
            - generic [ref=e301]: Filas por página
            - generic [ref=e304] [cursor=pointer]:
              - generic [ref=e306]:
                - generic [ref=e307]: "5"
                - combobox "5" [ref=e308]
              - generic [ref=e310]: arrow_drop_down
          - button [ref=e312] [cursor=pointer]:
            - img [ref=e314]: autorenew
  - generic:
    - dialog:
      - generic [ref=e316]:
        - generic [ref=e318]: Editar periodo Nota Técnica
        - generic [ref=e320]:
          - generic [ref=e321]:
            - generic [ref=e324]:
              - text: Periodo
              - generic [ref=e326]:
                - generic:
                  - generic:
                    - textbox [disabled]:
                      - /placeholder: Inserte
                      - text: 2027-1
            - generic [ref=e329]:
              - text: Valor
              - textbox [ref=e334]:
                - /placeholder: Inserte
                - text: 29/11/2024-1436-NT-P-40-0000000000000001
            - generic [ref=e338]:
              - text: Fecha inicio vigencia
              - generic [ref=e341] [cursor=pointer]:
                - generic [ref=e343]: calendar_month
                - textbox [ref=e345]:
                  - /placeholder: AAAA/MM/DD
                  - text: 2027/01/01
                - generic [ref=e347]: keyboard_arrow_down
            - generic [ref=e351]:
              - text: Fecha fin vigencia
              - generic [ref=e354] [cursor=pointer]:
                - generic [ref=e356]: calendar_month
                - textbox [ref=e358]:
                  - /placeholder: AAAA/MM/DD
                  - text: 2027/12/31
                - generic [ref=e360]: keyboard_arrow_down
            - generic [ref=e362]:
              - generic [ref=e363]: picture_as_pdf
              - generic [ref=e364]: nota_tecnica-2
              - button [ref=e365] [cursor=pointer]:
                - img [ref=e367]: download
          - generic [ref=e368]:
            - article [ref=e369]:
              - separator [ref=e370]
              - paragraph [ref=e371]: Información de Auditoría
            - article [ref=e372]:
              - generic [ref=e374]:
                - text: Fecha actualización
                - generic [ref=e376]:
                  - generic:
                    - generic:
                      - textbox [disabled]:
                        - /placeholder: Inserte
                        - text: 2026/05/19 14:02:56
            - article [ref=e377]:
              - generic [ref=e379]:
                - text: Usuario
                - generic [ref=e381]:
                  - generic:
                    - generic:
                      - textbox [disabled]:
                        - /placeholder: Inserte
                        - text: Marcelo.Duarte
          - generic [ref=e382]:
            - button "Cancelar" [ref=e383] [cursor=pointer]:
              - generic [ref=e385]: Cancelar
            - button "Guardar" [ref=e386] [cursor=pointer]:
              - generic [ref=e388]: Guardar
```

# Test source

```ts
  176 |         // Intenta regresar al listado maestro antes de declarar el parametro como no visible.
  177 |       }
  178 | 
  179 |       const pudoVolver = await this.clickAtrasSiExiste();
  180 |       if (!pudoVolver) {
  181 |         if (!this.estaEnRutaParametria()) {
  182 |           await this.open().catch(() => false);
  183 |           continue;
  184 |         }
  185 |         return false;
  186 |       }
  187 |     }
  188 | 
  189 |     return false;
  190 |   }
  191 | 
  192 |   async clickEditarParametroEnListadoActual(parametro: string): Promise<boolean> {
  193 |     await this.waitForParamTable();
  194 | 
  195 |     const row = await this.findRowByFirstCellValue(parametro);
  196 |     if (!row) {
  197 |       return false;
  198 |     }
  199 | 
  200 |     const botonEditar = row.locator(SELECTOR_BOTON_EDITAR_EN_FILA).first();
  201 |     if ((await botonEditar.count()) > 0) {
  202 |       await botonEditar.click({ timeout: 10_000 });
  203 |     } else {
  204 |       await row.locator(SELECTOR_BOTON_EN_FILA).first().click({ timeout: 10_000 });
  205 |     }
  206 | 
  207 |     await this.page.waitForLoadState('domcontentloaded').catch(() => {});
  208 |     await this.esperarDetalleParametro(parametro);
  209 |     return true;
  210 |   }
  211 | 
  212 |   async clickEditarPeriodo(periodo: string): Promise<boolean> {
  213 |     try {
  214 |       await this.waitForParamTable();
  215 |       await this.esperarFilasTablaVisibles();
  216 |       const row = await this.findRowByFirstCellValue(periodo);
  217 |       if (!row) {
  218 |         return false;
  219 |       }
  220 | 
  221 |       const botonEditar = row.locator(SELECTOR_BOTON_EDITAR_EN_FILA).first();
  222 |       if ((await botonEditar.count()) > 0) {
  223 |         await botonEditar.click({ timeout: 20_000 });
  224 |       } else {
  225 |         await row.locator(SELECTOR_BOTON_EN_FILA).first().click({ timeout: 20_000 });
  226 |       }
  227 |       return true;
  228 |     } catch {
  229 |       return false;
  230 |     }
  231 |   }
  232 | 
  233 |   private construirUrl(ruta: string): string {
  234 |     if (!this.url) {
  235 |       return ruta;
  236 |     }
  237 | 
  238 |     return `${this.url}${ruta}`;
  239 |   }
  240 | 
  241 |   async descargarArchivo(
  242 |     _context: unknown,
  243 |     _parametro: string,
  244 |     fileName: string
  245 |   ): Promise<string> {
  246 |     const downloadDir = path.resolve(process.cwd(), 'tmp_downloads', `${Date.now()}`);
  247 |     fs.mkdirSync(downloadDir, { recursive: true });
  248 | 
  249 |     const downloadPromise = this.page.waitForEvent('download', { timeout: 20_000 });
  250 |     await this.page.locator(SELECTOR_BOTON_DESCARGA).first().click();
  251 |     const download = await downloadPromise;
  252 | 
  253 |     const targetPath = path.resolve(downloadDir, download.suggestedFilename());
  254 |     await download.saveAs(targetPath);
  255 |     await this.downloadCurrentAttachment(fileName);
  256 |     return targetPath;
  257 |   }
  258 | 
  259 |   describirFilaParametro(row: Record<string, unknown>): string {
  260 |     const parametro = String(row.parametro ?? '').trim() || '[sin parametro]';
  261 |     const periodo = String(row.periodo ?? '').trim() || '[sin periodo]';
  262 |     const documento = String(row.documento ?? '').trim();
  263 | 
  264 |     return documento
  265 |       ? `parametro=${parametro}, periodo=${periodo}, documento=${documento}`
  266 |       : `parametro=${parametro}, periodo=${periodo}`;
  267 |   }
  268 | 
  269 |   async downloadCurrentAttachment(expectedFileName: string): Promise<void> {
  270 |     const downloadDir = path.resolve(process.cwd(), 'tmp_downloads', `${Date.now()}`);
  271 |     fs.mkdirSync(downloadDir, { recursive: true });
  272 | 
  273 |     const botonDescarga = this.page.locator(SELECTOR_BOTON_DESCARGA).first();
  274 |     await botonDescarga.waitFor({ state: 'visible', timeout: TIEMPO_ESPERA_DESCARGA_ARCHIVO_MS });
  275 | 
> 276 |     const downloadPromise = this.page.waitForEvent('download', { timeout: TIEMPO_ESPERA_DESCARGA_ARCHIVO_MS });
      |                                       ^ TimeoutError: page.waitForEvent: Timeout 12000ms exceeded while waiting for event "download"
  277 |     await botonDescarga.click({ timeout: TIEMPO_ESPERA_DESCARGA_ARCHIVO_MS, force: true });
  278 |     const download = await downloadPromise;
  279 | 
  280 |     const suggested = download.suggestedFilename();
  281 |     const targetPath = path.resolve(downloadDir, suggested);
  282 |     await download.saveAs(targetPath);
  283 | 
  284 |     try {
  285 |       expect(fs.existsSync(targetPath)).toBeTruthy();
  286 | 
  287 |       const expectedParts = path.parse(expectedFileName);
  288 |       const downloadedParts = path.parse(suggested);
  289 |       const normalizeDownloadedBaseName = (name: string) =>
  290 |         this.normalizarTextoAscii(name.replace(/(?:[-_ ]\(?\d+\)?)$/, ''));
  291 | 
  292 |       expect(normalizeDownloadedBaseName(downloadedParts.name)).toBe(
  293 |         this.normalizarTextoAscii(expectedParts.name)
  294 |       );
  295 |       expect(downloadedParts.ext.toLowerCase()).toBe(expectedParts.ext.toLowerCase());
  296 |     } finally {
  297 |       fs.rmSync(downloadDir, { recursive: true, force: true });
  298 |     }
  299 |   }
  300 | 
  301 |   async esperarGuardadoDeVigencia(periodo: string, mensajeNotificacionIgnorado = ''): Promise<void> {
  302 |     await this.esperarResultadoGuardadoDeVigencia(periodo, mensajeNotificacionIgnorado);
  303 |   }
  304 | 
  305 |   async esperarResultadoGuardadoDeVigencia(
  306 |     periodo: string,
  307 |     mensajeNotificacionIgnorado = ''
  308 |   ): Promise<ResultadoGuardadoVigencia> {
  309 |     const limite = Date.now() + 12_000;
  310 |     const inicioEspera = Date.now();
  311 |     let ultimaNotificacion = '';
  312 |     const notificacionIgnorada = this.normalizarTextoAscii(mensajeNotificacionIgnorado);
  313 | 
  314 |     while (Date.now() < limite) {
  315 |       const notificacionesVisibles = await this.obtenerTextosNotificacionesVisibles();
  316 |       const tiposVisibles = notificacionesVisibles.map((mensaje) => this.clasificarNotificacion(mensaje));
  317 |       const notificacionesNuevas = notificacionesVisibles
  318 |         .filter((mensaje) => this.normalizarTextoAscii(mensaje) !== notificacionIgnorada);
  319 |       ultimaNotificacion = notificacionesNuevas.at(-1) ?? notificacionesVisibles.at(-1) ?? '';
  320 |       const tiposNotificacion = notificacionesNuevas.map((mensaje) => this.clasificarNotificacion(mensaje));
  321 | 
  322 |       if (tiposNotificacion.includes('vigenciaConflictiva')) {
  323 |         return 'vigenciaConflictiva';
  324 |       }
  325 | 
  326 |       if (tiposNotificacion.includes('confirmacion') || tiposVisibles.includes('confirmacion')) {
  327 |         return 'guardado';
  328 |       }
  329 | 
  330 |       const puedeAsumirExitoSinNotificacion = Date.now() - inicioEspera >= 2_000;
  331 |       const formularioAbierto = await this.page
  332 |         .locator(this.selectorBotonPorTexto('Cancelar'))
  333 |         .first()
  334 |         .isVisible()
  335 |         .catch(() => false);
  336 |       const row = await this.findRowByFirstCellValue(periodo);
  337 |       if (puedeAsumirExitoSinNotificacion && row && !formularioAbierto) {
  338 |         return 'guardado';
  339 |       }
  340 | 
  341 |       if (tiposNotificacion.includes('error')) {
  342 |         throw new Error(`No fue posible guardar la vigencia ${periodo}: ${ultimaNotificacion}`);
  343 |       }
  344 | 
  345 |       await this.page.waitForTimeout(500);
  346 |     }
  347 | 
  348 |     throw new Error(
  349 |       `No se confirmo el guardado de la vigencia ${periodo} dentro del tiempo esperado.` +
  350 |       (ultimaNotificacion ? ` Ultima notificacion visible: ${ultimaNotificacion}` : '')
  351 |     );
  352 |   }
  353 | 
  354 |   async estaEnListadoMaestro(): Promise<boolean> {
  355 |     const contenido = this.normalizarTextoAscii(
  356 |       await this.page.locator(SELECTOR_CUERPO).innerText().catch(() => '')
  357 |     );
  358 |     const headers = ['tipo variable', 'tipo dato', 'acciones'];
  359 | 
  360 |     if (!headers.every((header) => contenido.includes(header))) {
  361 |       return false;
  362 |     }
  363 | 
  364 |     const primerValor = await this.page
  365 |       .locator(SELECTOR_PRIMERA_CELDA_FILAS_TABLA)
  366 |       .first()
  367 |       .innerText()
  368 |       .catch(() => '');
  369 | 
  370 |     return this.normalizarTextoAscii(primerValor) !== '';
  371 |   }
  372 | 
  373 |   async findRowByFirstCellValue(expectedValue: string): Promise<Locator | null> {
  374 |     const valorTrimmed = expectedValue.trim();
  375 |     const filaDirecta = this.page
  376 |       .locator(this.selectorFilaTablaPorPrimeraCelda(valorTrimmed))
```