#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtxmlpatterns
Version  : 5.14.2
Release  : 22
URL      : https://download.qt.io/official_releases/qt/5.14/5.14.2/submodules/qtxmlpatterns-everywhere-src-5.14.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.14/5.14.2/submodules/qtxmlpatterns-everywhere-src-5.14.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0 W3C
Requires: qtxmlpatterns-bin = %{version}-%{release}
Requires: qtxmlpatterns-lib = %{version}-%{release}
Requires: qtxmlpatterns-license = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5Xml)

%description
qtokenautomaton is a token generator, that generates a simple, Unicode aware
tokenizer for C++ that uses the Qt API.

%package bin
Summary: bin components for the qtxmlpatterns package.
Group: Binaries
Requires: qtxmlpatterns-license = %{version}-%{release}

%description bin
bin components for the qtxmlpatterns package.


%package dev
Summary: dev components for the qtxmlpatterns package.
Group: Development
Requires: qtxmlpatterns-lib = %{version}-%{release}
Requires: qtxmlpatterns-bin = %{version}-%{release}
Provides: qtxmlpatterns-devel = %{version}-%{release}
Requires: qtxmlpatterns = %{version}-%{release}

%description dev
dev components for the qtxmlpatterns package.


%package examples
Summary: examples components for the qtxmlpatterns package.
Group: Default
Requires: qtxmlpatterns-dev = %{version}-%{release}

%description examples
examples components for the qtxmlpatterns package.


%package lib
Summary: lib components for the qtxmlpatterns package.
Group: Libraries
Requires: qtxmlpatterns-license = %{version}-%{release}

%description lib
lib components for the qtxmlpatterns package.


%package license
Summary: license components for the qtxmlpatterns package.
Group: Default

%description license
license components for the qtxmlpatterns package.


%prep
%setup -q -n qtxmlpatterns-everywhere-src-5.14.2
cd %{_builddir}/qtxmlpatterns-everywhere-src-5.14.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1586202723
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtxmlpatterns
cp %{_builddir}/qtxmlpatterns-everywhere-src-5.14.2/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtxmlpatterns/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtxmlpatterns-everywhere-src-5.14.2/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtxmlpatterns/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qtxmlpatterns-everywhere-src-5.14.2/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtxmlpatterns/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qtxmlpatterns-everywhere-src-5.14.2/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtxmlpatterns/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
cp %{_builddir}/qtxmlpatterns-everywhere-src-5.14.2/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtxmlpatterns/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/qtxmlpatterns-everywhere-src-5.14.2/src/xmlpatterns/schema/schemas/xml.xsd-LICENSE %{buildroot}/usr/share/package-licenses/qtxmlpatterns/f42f72f6a943f67dd3793a2cf4eb933d44fa2dde
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xmlpatterns
/usr/bin/xmlpatternsvalidator

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractdatetime_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractduration_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractfloat_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractfloat_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractfloatcasters_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractfloatcasters_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractfloatmathematician_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractfloatmathematician_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractfunctionfactory_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractnodetest_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractxmlforwarditerator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractxmlnodemodel_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractxmlpullprovider_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qabstractxmlreceiver_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qacceliterators_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qacceltree_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qacceltreebuilder_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qacceltreebuilder_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qacceltreeresourceloader_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qaccessorfns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qaggregatefns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qaggregator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qandexpression_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qanyitemtype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qanynodetype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qanysimpletype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qanytype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qanyuri_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qapplytemplate_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qargumentconverter_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qargumentreference_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qarithmeticexpression_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qassemblestringfns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomiccaster_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomiccasterlocator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomiccasterlocators_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomiccasters_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomiccomparator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomiccomparatorlocator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomiccomparatorlocators_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomiccomparators_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomicmathematician_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomicmathematicianlocator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomicmathematicianlocators_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomicmathematicians_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomicstring_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomictype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomictypedispatch_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qatomizer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qattributeconstructor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qattributenamevalidator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qautoptr_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qaxisstep_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qbase64binary_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qbasictypesfactory_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qboolean_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qbooleanfns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qbuiltinatomictype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qbuiltinatomictypes_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qbuiltinnodetype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qbuiltinnodetype_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qbuiltintypes_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcachecells_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcachingiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcallsite_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcalltargetdescription_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcalltemplate_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcardinality_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcardinalityverifier_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcastableas_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcastas_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcastingplatform_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcastingplatform_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcollationchecker_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcoloringmessagehandler_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcoloroutput_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcombinenodes_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcommentconstructor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcommonnamespaces_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcommonsequencetypes_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcommonvalues_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcomparescaseaware_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcomparestringfns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcomparingaggregator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcomparingaggregator_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcomparisonfactory_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcomparisonplatform_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcomparisonplatform_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcompressedwhitespace_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcomputednamespaceconstructor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qconstructorfunctionsfactory_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcontextfns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcontextitem_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcontextnodechecker_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcopyof_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcppcastinghelper_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcurrentfn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcurrentitemcontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qcurrentitemstore_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdate_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdatetimefn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdatetimefns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdatetimefns_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdaytimeduration_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdecimal_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdeduplicateiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdeepequalfn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdelegatingdynamiccontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdelegatingnamespaceresolver_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdelegatingstaticcontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qderivedinteger_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qderivedstring_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdeviceresourceloader_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdistinctiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdocumentconstructor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdocumentcontentvalidator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdocumentfn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdocumentprojector_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qduration_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdynamiccontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qdynamiccontextstore_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qebvextractor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qebvtype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qelementavailablefn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qelementconstructor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qemptycontainer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qemptyiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qemptysequence_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qemptysequencetype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qerrorfn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qevaluationcache_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qevaluationcache_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qexceptiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qexpression_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qexpressiondispatch_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qexpressionfactory_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qexpressionsequence_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qexpressionvariablereference_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qexternalvariableloader_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qexternalvariablereference_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qfirstitempredicate_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qfocus_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qforclause_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qfunctionargument_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qfunctionavailablefn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qfunctioncall_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qfunctionfactory_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qfunctionfactorycollection_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qfunctionsignature_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qgday_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qgeneralcomparison_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qgenerateidfn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qgenericdynamiccontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qgenericnamespaceresolver_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qgenericpredicate_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qgenericsequencetype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qgenericstaticcontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qgmonth_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qgmonthday_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qgyear_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qgyearmonth_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qhexbinary_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qifthenclause_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qindexofiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qinsertioniterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qinstanceof_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qinteger_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qintersectiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qiodevicedelegate_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qitem_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qitemmappingiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qitemtype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qitemverifier_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qletclause_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qliteral_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qliteralsequence_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qlocalnametest_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qmaintainingreader_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qmaintainingreader_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qmultiitemtype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnamedschemacomponent_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnamepool_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnamespacebinding_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnamespaceconstructor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnamespacenametest_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnamespaceresolver_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnamespacesupport_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qncnameconstructor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnetworkaccessdelegator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnodebuilder_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnodecomparison_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnodefns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnodenamespaceresolver_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnodesort_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnonetype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnumericfns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qnumerictype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qoperandsiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qoptimizationpasses_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qoptimizerblocks_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qoptimizerframework_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qorderby_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qorexpression_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qoutputvalidator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qpaircontainer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qparentnodeaxis_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qparsercontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qpath_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qpatternistlocale_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qpatternmatchingfns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qpatternplatform_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qpositionalvariablereference_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qprimitives_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qprocessinginstructionconstructor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qprojectedexpression_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qpullbridge_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qqnameconstructor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qqnamefns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qqnametest_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qqnamevalue_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qquantifiedexpression_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qquerytransformparser_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qrangeexpression_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qrangeiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qrangevariablereference_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qreceiverdynamiccontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qreferencecountedvalue_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qremovaliterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qreportcontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qresolveurifn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qresourcedelegator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qresourceloader_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qreturnorderby_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qschemacomponent_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qschemadatetime_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qschemanumeric_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qschematime_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qschematype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qschematypefactory_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsequencefns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsequencegeneratingfns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsequencemappingiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsequencereceiver_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsequencetype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsimplecontentconstructor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsinglecontainer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsingletoniterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsorttuple_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsourcelocationreflection_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstackcontextbase_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstackcontextbase_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstaticbaseuricontainer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstaticbaseuricontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstaticbaseuristore_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstaticcompatibilitycontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstaticcompatibilitystore_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstaticcontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstaticcurrentcontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstaticfocuscontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstaticnamespacecontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstaticnamespacescontainer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qstringvaluefns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsubsequenceiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsubstringfns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qsystempropertyfn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtemplate_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtemplateinvoker_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtemplatemode_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtemplateparameterreference_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtemplatepattern_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtextnodeconstructor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtimezonefns_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtocodepointsiterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtokenizer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtokenrevealer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtokensource_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtokenvalue_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtracefn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtreatas_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtriplecontainer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtruthpredicate_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtxmlpatterns-config_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtypeavailablefn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qtypechecker_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qunaryexpression_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qunioniterator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qunlimitedcontainer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qunparsedentitypublicidfn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qunparsedentityurifn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qunparsedtextavailablefn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qunparsedtextfn_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qunresolvedvariablereference_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/quntyped_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/quntypedatomic_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/quntypedatomicconverter_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/quriloader_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/quserfunction_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/quserfunctioncallsite_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qvalidate_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qvalidationerror_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qvaluecomparison_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qvaluefactory_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qvariabledeclaration_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qvariableloader_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qvariablereference_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qwithparam_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxmldebug_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxmlpatternistcli_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxmlquery_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxmlresultitems_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxmlschema_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxmlschemavalidator_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxmlserializer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxpath10corefunctions_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxpath20corefunctions_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxpathhelper_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxquerytokenizer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdalternative_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdannotated_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdannotation_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdapplicationinformation_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdassertion_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdattribute_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdattributegroup_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdattributereference_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdattributeterm_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdattributeuse_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdcomplextype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsddocumentation_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdelement_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdfacet_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdidcache_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdidchelper_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdidentityconstraint_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdinstancereader_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdmodelgroup_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdnotation_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdparticle_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdparticlechecker_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdreference_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdschema_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdschemachecker_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdschemacontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdschemadebugger_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdschemahelper_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdschemamerger_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdschemaparser_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdschemaparsercontext_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdschemaresolver_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdschematoken_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdschematypesfactory_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdsimpletype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdstatemachine_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdstatemachine_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdstatemachinebuilder_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdterm_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdtypechecker_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsduserschematype_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsduserschematype_tpl_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdvalidatedxmlnodemodel_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdvalidatinginstancereader_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdwildcard_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsdxpathexpression_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxslt20corefunctions_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsltnodetest_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxsltsimplecontentconstructor_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxslttokenizer_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qxslttokenlookup_p.h
/usr/include/qt5/QtXmlPatterns/5.14.2/QtXmlPatterns/private/qyearmonthduration_p.h
/usr/include/qt5/QtXmlPatterns/QAbstractMessageHandler
/usr/include/qt5/QtXmlPatterns/QAbstractUriResolver
/usr/include/qt5/QtXmlPatterns/QAbstractXmlNodeModel
/usr/include/qt5/QtXmlPatterns/QAbstractXmlReceiver
/usr/include/qt5/QtXmlPatterns/QSimpleXmlNodeModel
/usr/include/qt5/QtXmlPatterns/QSourceLocation
/usr/include/qt5/QtXmlPatterns/QXmlFormatter
/usr/include/qt5/QtXmlPatterns/QXmlItem
/usr/include/qt5/QtXmlPatterns/QXmlName
/usr/include/qt5/QtXmlPatterns/QXmlNamePool
/usr/include/qt5/QtXmlPatterns/QXmlNodeModelIndex
/usr/include/qt5/QtXmlPatterns/QXmlQuery
/usr/include/qt5/QtXmlPatterns/QXmlResultItems
/usr/include/qt5/QtXmlPatterns/QXmlSchema
/usr/include/qt5/QtXmlPatterns/QXmlSchemaValidator
/usr/include/qt5/QtXmlPatterns/QXmlSerializer
/usr/include/qt5/QtXmlPatterns/QtXmlPatterns
/usr/include/qt5/QtXmlPatterns/QtXmlPatternsDepends
/usr/include/qt5/QtXmlPatterns/QtXmlPatternsVersion
/usr/include/qt5/QtXmlPatterns/qabstractmessagehandler.h
/usr/include/qt5/QtXmlPatterns/qabstracturiresolver.h
/usr/include/qt5/QtXmlPatterns/qabstractxmlnodemodel.h
/usr/include/qt5/QtXmlPatterns/qabstractxmlreceiver.h
/usr/include/qt5/QtXmlPatterns/qsimplexmlnodemodel.h
/usr/include/qt5/QtXmlPatterns/qsourcelocation.h
/usr/include/qt5/QtXmlPatterns/qtxmlpatterns-config.h
/usr/include/qt5/QtXmlPatterns/qtxmlpatternsglobal.h
/usr/include/qt5/QtXmlPatterns/qtxmlpatternsversion.h
/usr/include/qt5/QtXmlPatterns/qxmlformatter.h
/usr/include/qt5/QtXmlPatterns/qxmlname.h
/usr/include/qt5/QtXmlPatterns/qxmlnamepool.h
/usr/include/qt5/QtXmlPatterns/qxmlquery.h
/usr/include/qt5/QtXmlPatterns/qxmlresultitems.h
/usr/include/qt5/QtXmlPatterns/qxmlschema.h
/usr/include/qt5/QtXmlPatterns/qxmlschemavalidator.h
/usr/include/qt5/QtXmlPatterns/qxmlserializer.h
/usr/lib64/cmake/Qt5XmlPatterns/Qt5XmlPatternsConfig.cmake
/usr/lib64/cmake/Qt5XmlPatterns/Qt5XmlPatternsConfigVersion.cmake
/usr/lib64/libQt5XmlPatterns.prl
/usr/lib64/libQt5XmlPatterns.so
/usr/lib64/pkgconfig/Qt5XmlPatterns.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_xmlpatterns.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_xmlpatterns_private.pri

%files examples
%defattr(-,root,root,-)
/usr/share/qt5/examples/xmlpatterns/README
/usr/share/qt5/examples/xmlpatterns/filetree/filetree.cpp
/usr/share/qt5/examples/xmlpatterns/filetree/filetree.h
/usr/share/qt5/examples/xmlpatterns/filetree/filetree.pro
/usr/share/qt5/examples/xmlpatterns/filetree/forms/mainwindow.ui
/usr/share/qt5/examples/xmlpatterns/filetree/main.cpp
/usr/share/qt5/examples/xmlpatterns/filetree/mainwindow.cpp
/usr/share/qt5/examples/xmlpatterns/filetree/mainwindow.h
/usr/share/qt5/examples/xmlpatterns/filetree/queries.qrc
/usr/share/qt5/examples/xmlpatterns/filetree/queries/listCPPFiles.xq
/usr/share/qt5/examples/xmlpatterns/filetree/queries/wholeTree.xq
/usr/share/qt5/examples/xmlpatterns/recipes/files/allRecipes.xq
/usr/share/qt5/examples/xmlpatterns/recipes/files/cookbook.xml
/usr/share/qt5/examples/xmlpatterns/recipes/files/liquidIngredientsInSoup.xq
/usr/share/qt5/examples/xmlpatterns/recipes/files/mushroomSoup.xq
/usr/share/qt5/examples/xmlpatterns/recipes/files/preparationLessThan30.xq
/usr/share/qt5/examples/xmlpatterns/recipes/files/preparationTimes.xq
/usr/share/qt5/examples/xmlpatterns/recipes/forms/querywidget.ui
/usr/share/qt5/examples/xmlpatterns/recipes/main.cpp
/usr/share/qt5/examples/xmlpatterns/recipes/querymainwindow.cpp
/usr/share/qt5/examples/xmlpatterns/recipes/querymainwindow.h
/usr/share/qt5/examples/xmlpatterns/recipes/recipes.pro
/usr/share/qt5/examples/xmlpatterns/recipes/recipes.qrc
/usr/share/qt5/examples/xmlpatterns/schema/files/contact.xsd
/usr/share/qt5/examples/xmlpatterns/schema/files/invalid_contact.xml
/usr/share/qt5/examples/xmlpatterns/schema/files/invalid_order.xml
/usr/share/qt5/examples/xmlpatterns/schema/files/invalid_recipe.xml
/usr/share/qt5/examples/xmlpatterns/schema/files/order.xsd
/usr/share/qt5/examples/xmlpatterns/schema/files/recipe.xsd
/usr/share/qt5/examples/xmlpatterns/schema/files/valid_contact.xml
/usr/share/qt5/examples/xmlpatterns/schema/files/valid_order.xml
/usr/share/qt5/examples/xmlpatterns/schema/files/valid_recipe.xml
/usr/share/qt5/examples/xmlpatterns/schema/main.cpp
/usr/share/qt5/examples/xmlpatterns/schema/mainwindow.cpp
/usr/share/qt5/examples/xmlpatterns/schema/mainwindow.h
/usr/share/qt5/examples/xmlpatterns/schema/schema.pro
/usr/share/qt5/examples/xmlpatterns/schema/schema.qrc
/usr/share/qt5/examples/xmlpatterns/schema/schema.ui
/usr/share/qt5/examples/xmlpatterns/shared/xmlsyntaxhighlighter.cpp
/usr/share/qt5/examples/xmlpatterns/shared/xmlsyntaxhighlighter.h
/usr/share/qt5/examples/xmlpatterns/xmlpatterns.pro
/usr/share/qt5/examples/xmlpatterns/xquery/globalVariables/globals.cpp
/usr/share/qt5/examples/xmlpatterns/xquery/globalVariables/globals.gccxml
/usr/share/qt5/examples/xmlpatterns/xquery/globalVariables/globals.html
/usr/share/qt5/examples/xmlpatterns/xquery/globalVariables/reportGlobals.xq
/usr/share/qt5/examples/xmlpatterns/xquery/xquery.pro

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5XmlPatterns.so.5
/usr/lib64/libQt5XmlPatterns.so.5.14
/usr/lib64/libQt5XmlPatterns.so.5.14.2
/usr/lib64/qt5/qml/QtQuick/XmlListModel/libqmlxmllistmodelplugin.so
/usr/lib64/qt5/qml/QtQuick/XmlListModel/plugins.qmltypes
/usr/lib64/qt5/qml/QtQuick/XmlListModel/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtxmlpatterns/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qtxmlpatterns/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtxmlpatterns/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtxmlpatterns/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
/usr/share/package-licenses/qtxmlpatterns/f42f72f6a943f67dd3793a2cf4eb933d44fa2dde
/usr/share/package-licenses/qtxmlpatterns/f45ee1c765646813b442ca58de72e20a64a7ddba
